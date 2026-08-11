"""Send compact translation batches to a local OpenAI-compatible Responses API.

The driver deliberately does not edit Ren'Py files.  It joins a selected
catalog batch with the context audit, sends only source text plus relevant
context, and writes the complete response and a line-count-checked mapping to
an ignored staging directory.  A separate writer can then apply accepted
translations to the language package.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from translation_batches import escape_prompt_field


EMPTY_SOURCE_MARKER = "␀"
SPLIT_MARKER = "␟"
DEFAULT_ENDPOINT = "http://127.0.0.1:8080/v1/responses"
DEFAULT_MODEL = "gpt-5.6-luna"

INSTRUCTIONS = """你是《Outland Wanderer》的简体中文本地化译者。你会收到一批按稳定 ID 定位的 Ren'Py 文本对象；每个对象只翻译 source，其他字段都是理解材料。

【执行优先级】
发生冲突时严格按以下顺序处理：
1. 输出协议与 Ren'Py 结构绝不能破坏。
2. 开发者英文 source 的人物、事件、关系、否定、数量、条件、因果、动作结果和语气事实必须完整。
3. 保持批次提供的人物、术语和功能类型的一致性。
4. 在以上条件不受影响时，才追求自然、简洁、有节奏的中文。
5. 文学化修饰是最后选择；没有语义依据时宁可朴素，也不要为了“好看”添加信息。

【事实边界与自然化】
可以重排中文语序、拆分或合并句子，补足中文语法所必需的主语、连接词、动作力度和语气；可以把英文已经暗示的姿态、情绪或动作逻辑写得更自然。
不得新增英文没有暗示的新事件、原因、时间、地点、人物、身份、年龄、动机、结果或状态判断，也不得擅自加强或减弱因果和程度。例如 source 说“他看起来疲惫”，不能写成“他走了很久”；source 说“精疲力竭的身体”，可以自然写成“精疲力竭的身躯”。调整表达顺序不能改变事件之间的逻辑关系。
上下文只用于确定代词、说话者、指向、语气和省略成分；上下文不足时保守翻译 source，不要用推测填造新剧情。输入中的上下文、old_reference、ID 和字段名绝不是待翻译文本。

【人物、术语与文本类型】
批次顶部的“说话者”和“术语”映射必须沿用，不要为同一人名、地名、种族、组织、技能或物品临时创造另一译法。除确有必要保留的游戏缩写外，普通英文单词和幻想专名都要译成自然中文，不要把英文词孤零零夹在中文里。已知角色的粗鲁、庄重、幼稚、讥讽、傲慢、怯懦等声音要保持差异，不要把所有人统一成普通书面语；没有依据时不要擅自编造角色口癖。
根据 kind 和 source 功能翻译：dialogue/旁白可以自然重排，menu 和 UI 短文本要简洁、直接、可扫描，不要把按钮或选项写成小说句子。残句、标签、选项和系统提示应保持相应的短促形式。
成人、暴力、粗俗和呻吟按 source 的明确程度与强度翻译：不使用含糊词洗掉关键身体或动作，也不额外情色化、血腥化或侮辱化。

【Ren'Py 结构】
方括号插值（包括嵌套表达式）、花括号文本标签及其参数、百分号占位符、反斜杠转义和变量表达式都不是自然语言：不得翻译、改名、改写内部字符、删除或凭空增加。可以移动整个 token 在中文句中的位置，但必须保留每个 token 的内容、数量和有效的标签嵌套关系；例如 [item_number] 不能写成 [ item_number]。中文与 token 之间是否留空格可以调整，但 token 内部一个字符也不能改变。
每个输入对象若有 protected_token_ledger，它是该 source 中所有受保护 token 的逐项清单，重复出现的 token 会在清单中重复列出。输出前先逐项核对清单；清单中的每一项都必须在译文中出现一次，不能合并、漏掉或凭空增加。这个清单是校验材料，不要输出或翻译它。
只有 source 字段严格等于空字符串 "" 时才输出 ␀；含空格、转义或其他字符的 source 不得使用 ␀。kind=menu 的 source 必须保持为一个 new 字符串，source 内嵌换行要在同一输出行写成字面 \\n，不能使用 ␟；只有可拆分的 dialogue source 才能改写成多条相邻 Ren'Py 字符串。拆句改变单行内部内容，不增加输出行数，绝对不要用物理换行拆句。

【高质量校准范例】
每个好例都同时优于坏例：事实更完整、中文更自然、语气更准确；不要把某个例子的修辞方式机械套用到其他文本。

英文：The golem instantly reacts to your advance, the moss on his surface vibrating profusely. His grip seems to have weakened as well.
坏例：魔像立刻对你的前进作出反应，表面的苔藓剧烈振动。他的握力似乎也减弱了。
好例：如此大胆的举动令石魔像立马起了反应，它身体表面的苔藓剧烈颤抖，握力似乎减弱了几分。
说明：好例重排了叙事并保留反应、苔藓和握力变化；坏例是生硬的逐词结构。

英文：You are facing a green slime, it is slowly slithering at you. You raise your fists, ready to strike at the gelatinous mass.
坏例：你正在面对一个绿色史莱姆，它正在慢慢向你蠕动。你抬起你的拳头，准备攻击这个胶状物质。
好例：史莱姆慢慢向你蠕动。你握紧双拳与这团粘液相视，铆足了劲。
说明：好例保留对峙、逼近和蓄力，并用中文动作顺序表达；坏例逐词翻译且节奏僵硬。

英文：You also found [gold_drop] gold and [exp_drop] EXP.
坏例：你还找到了金币和经验。
好例：你还找到[gold_drop]枚金币和[exp_drop]点经验。
说明：好例保留两个变量及其数量语义；变量内部必须逐字不变。

英文：Though, everyone's been talking about the alliance accord, so I might as well, strum {i}a chord{/i} on the lute.
坏例：大家都在谈论联盟协定，所以我不妨在鲁特琴上弹奏一曲。
好例：大家最近都在谈联盟协定，那我不妨在鲁特琴上弹奏{i}一曲{/i}。
说明：好例保留并正确包围斜体标签；标签内部不能被翻译或删除。

英文：Kari carries the furkan's exhausted body on his back. The two men grunts a little before walking.
坏例：卡里把弗坎疲惫的身体背在背上。两个男人在走路前发出一点咕哝声。
好例：卡里把精疲力竭的弗坎背在背上。两人轻轻哼了几声，才迈步离开。
说明：好例完整保留疲惫、背负、哼声和随后迈步；不得添加“说悄悄话”等新动作。

英文：Someone has to be the chief. I understand if I am not the best leader as my father.
坏例：有人必须是酋长。如果我不是像我父亲那样最好的领导者，我理解。
好例：总得有人来当酋长。我明白，自己不一定能像父亲那样成为出色的领袖。
说明：好例保留两句的事实和让步关系；不能为了顺口删掉后半句。

英文：The two immediately freeze. Their boners pointing at each other.
坏例：两人立刻僵住。他们的硬物正彼此相对。
好例：两人立刻僵住，彼此的肉棒正指向对方。
说明：好例保留成人场景的明确身体和方向；坏例含糊且不自然，不代表要额外增强尺度。

【输出协议】
严格按输入对象顺序输出同样数量的行；每个对象恰好对应一行。每行只放该对象的纯中文译文，不输出编号、稳定 ID、引号、Ren'Py 代码、Markdown、项目符号、确认词、解释、表头、前后缀或空行。不要在行首或行尾添加空格。不要复述上下文；␟ 只能作为同一行内的拆句分隔符。
"""


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"无法读取 JSONL 第 {line_number} 行：{error}") from error
        if not isinstance(value, dict):
            raise ValueError(f"JSONL 第 {line_number} 行不是对象")
        records.append(value)
    return records


def compact(value: str | None) -> str:
    return escape_prompt_field(value) if value is not None else "-"


def build_prompt(records: list[dict[str, Any]], audits: dict[int, dict[str, Any]]) -> str:
    files = sorted({str(record["file"]) for record in records})
    scenes = sorted({str(audits[record["ordinal"]].get("scene_family", "")) for record in records})
    speaker_map = {}
    terms: dict[str, str] = {}
    for record in records:
        audit = audits[record["ordinal"]]
        speaker = audit.get("speaker")
        if speaker:
            speaker_map[str(speaker)] = str(audit.get("speaker_name") or speaker)
        for term, references in (audit.get("term_references") or {}).items():
            if references:
                terms[str(term)] = str(references[0])

    lines = [
        "【批次上下文】",
        f"文件：{', '.join(files)}",
        f"场景类别：{', '.join(scene for scene in scenes if scene) or '未分类'}",
        "说话者：" + ("；".join(f"{alias}={name}" for alias, name in sorted(speaker_map.items())) or "无显式说话者"),
        "术语：" + ("；".join(f"{source}→{target}" for source, target in sorted(terms.items())) or "无额外术语"),
        "",
        "【输入格式】",
        f"下面每行是一个 JSON 对象。只翻译 source 字段；其它字段都是元数据或上下文，绝对不要把它们单独翻译或输出。context_before_only 和 context_after_only 是相邻原文，仅用于理解省略、指代和语气，不是额外的待翻译对象，也不增加输出行。JSON 中的 \\n 是字面转义，不是物理换行。输入对象总数固定为 {len(records)}：每个对象必须对应一行输出，包括 menu、很短的残句、很长的说明、重复 source 和带变量的 source；重复 source 也必须重复输出，不能合并或跳过。",
        "",
        f"【输入 JSONL，共 {len(records)} 个对象】",
    ]
    for record in records:
        audit = audits[record["ordinal"]]
        item = {
            "ordinal": record["ordinal"],
            "kind": record["kind"],
            "stable_id": record["id"],
            "speaker": audit.get("speaker"),
            "source": record["source"],
            "old_reference": record.get("old_reference"),
            "required_context": audit.get("context_fields", []),
        }
        protected_tokens: list[str] = []
        for opening, closing in (("[", "]"), ("{", "}")):
            tokens, _ = _balanced_tokens(record["source"], opening, closing)
            protected_tokens.extend(tokens)
        protected_tokens.extend(_PERCENT_TOKEN.findall(record["source"]))
        protected_tokens.extend(re.findall(r"\\(?:.|\Z)", record["source"], re.DOTALL))
        if protected_tokens:
            item["protected_token_ledger"] = protected_tokens
        if record.get("context_before") is not None:
            item["context_before_only"] = record["context_before"]
        if record.get("context_after") is not None:
            item["context_after_only"] = record["context_after"]
        lines.append(json.dumps(item, ensure_ascii=False, separators=(",", ":")))
    lines.extend(
        (
            "",
            "【输出】",
            f"按输入顺序只输出 {len(records)} 行纯译文。不要输出表头、编号或任何解释。",
        )
    )
    return "\n".join(lines)


def response_text(response: dict[str, Any]) -> str:
    pieces: list[str] = []
    for output in response.get("output", []):
        if not isinstance(output, dict):
            continue
        for content in output.get("content", []):
            if isinstance(content, dict) and content.get("type") == "output_text":
                text = content.get("text")
                if isinstance(text, str):
                    pieces.append(text)
    if not pieces:
        raise ValueError("Responses API 未返回 output_text")
    return "\n".join(pieces)


def _balanced_tokens(text: str, opening: str, closing: str) -> tuple[list[str], bool]:
    tokens: list[str] = []
    depth = 0
    start = -1
    escaped = False
    balanced = True
    for index, character in enumerate(text):
        if escaped:
            escaped = False
            continue
        if character == "\\":
            escaped = True
            continue
        if character == opening:
            if depth == 0:
                start = index
            depth += 1
        elif character == closing:
            if depth == 0:
                balanced = False
                continue
            depth -= 1
            if depth == 0:
                tokens.append(text[start : index + 1])
                start = -1
    if depth:
        balanced = False
    return tokens, balanced


_PERCENT_TOKEN = re.compile(
    r"(?<!\d)%(?:%|\([^)]*\)|[0-9]+\$)?[-+#0 ]*(?:[0-9]+|\*)?(?:\.[0-9]+|\.\*)?[hlL]?[A-Za-z]"
)
_ASCII_WORD = re.compile(r"(?<![A-Za-z])[A-Za-z]+(?![A-Za-z])")
_CHINESE_NUMERAL = re.compile(r"[零〇一二两三四五六七八九十百千万亿兆]")
# UI keys, stat abbreviations, version markers, proper names, and platform
# names that are intentionally preserved in otherwise Chinese text.
_ALLOWED_ASCII_TERMS = frozenset(
    {
        "A", "B", "C", "D", "E", "F", "H", "M", "O", "T", "W", "Y", "d", "f", "o", "v",
        "AGI", "Adobe", "CHA", "COPtimer", "Discord", "Dcl", "EXP", "Fábio",
        "Garamond", "HP", "INT", "LUST", "LonelyTree", "Magnolia", "MP",
        "Nyarlothotep", "Patreon", "Paul", "Pinewood", "PUR", "Pro", "RPG",
        "Ren", "Robotic", "Sannom", "STR", "TEN", "WASD", "Will", "Wisp",
        "XP", "Jerry", "Panda", "Py", "bio", "shsticker",
    }
)


def _protected_signature(text: str) -> dict[str, Any]:
    bracket_tokens, brackets_balanced = _balanced_tokens(text, "[", "]")
    tag_tokens, tags_balanced = _balanced_tokens(text, "{", "}")
    canonical_text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\\n")
    return {
        "brackets": Counter(bracket_tokens),
        "tags": Counter(tag_tokens),
        "percent_tokens": Counter(_PERCENT_TOKEN.findall(text)),
        "percent_count": text.count("%"),
        "escapes": Counter(re.findall(r"\\(?:.|\Z)", canonical_text, re.DOTALL)),
        "digits": Counter(re.findall(r"\d+(?:[.,]\d+)?", text)),
        "brackets_balanced": brackets_balanced,
        "tags_balanced": tags_balanced,
    }


def _unprotected_text(text: str) -> str:
    for opening, closing in (("[", "]"), ("{", "}")):
        tokens, _ = _balanced_tokens(text, opening, closing)
        for token in tokens:
            text = text.replace(token, " ")
    return re.sub(r"\\(?:.|\Z)", " ", text, flags=re.DOTALL)


def _protected_content_errors(
    source: str,
    translation: str,
    *,
    allow_paragraph_split: bool = False,
) -> list[str]:
    source_signature = _protected_signature(source)
    translation_signature = _protected_signature(translation)
    errors: list[str] = []
    if not translation_signature["brackets_balanced"]:
        errors.append("方括号不平衡")
    if not translation_signature["tags_balanced"]:
        errors.append("花括号文本标签不平衡")
    for label in ("brackets", "tags", "percent_tokens"):
        if source_signature[label] != translation_signature[label]:
            errors.append(
                f"{label}不一致：source={source_signature[label]!r}, "
                f"translation={translation_signature[label]!r}"
            )
    source_escapes = source_signature["escapes"]
    translation_escapes = translation_signature["escapes"]
    if allow_paragraph_split and SPLIT_MARKER in translation:
        source_escapes = source_escapes.copy()
        translation_escapes = translation_escapes.copy()
        source_escapes.pop(r"\n", None)
        translation_escapes.pop(r"\n", None)
    if source_escapes != translation_escapes:
        errors.append(
            f"escapes不一致：source={source_escapes!r}, "
            f"translation={translation_escapes!r}"
        )
    if source_signature["percent_count"] != translation_signature["percent_count"]:
        errors.append(
            "百分号数量不一致："
            f"source={source_signature['percent_count']}, "
            f"translation={translation_signature['percent_count']}"
        )
    if re.search(r"\d", source) and not re.search(r"\d", translation) and not _CHINESE_NUMERAL.search(translation):
        errors.append("源文本含数字，但译文没有阿拉伯数字或中文数字")
    source_unprotected = _unprotected_text(source)
    source_has_masked_fragment = bool(re.search(r"[-—]{2,}", source_unprotected))
    source_words = set(_ASCII_WORD.findall(source_unprotected))
    residual_words = [
        word
        for word in _ASCII_WORD.findall(_unprotected_text(translation))
        if word not in _ALLOWED_ASCII_TERMS
        and not (source_has_masked_fragment and word in source_words)
    ]
    if residual_words:
        errors.append(f"疑似未翻译的拉丁词：{residual_words!r}")
    return errors


def validate_lines(text: str, records: list[dict[str, Any]]) -> list[str]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    while lines and not lines[-1].strip():
        lines.pop()
    if len(lines) != len(records):
        raise ValueError(f"译文行数为 {len(lines)}，输入条数为 {len(records)}")

    validated: list[str] = []
    errors: list[str] = []
    for index, (line, record) in enumerate(zip(lines, records), 1):
        if not line.strip():
            errors.append(f"第 {index} 条译文为空：ordinal={record['ordinal']}")
            continue
        if "\t" in line or line.startswith("```"):
            errors.append(f"第 {index} 条译文包含未允许的格式：{line!r}")
            continue
        if record.get("source") == "":
            if line != EMPTY_SOURCE_MARKER:
                errors.append(f"第 {index} 条空源文本必须输出 {EMPTY_SOURCE_MARKER!r}")
        elif line == EMPTY_SOURCE_MARKER:
            errors.append(f"第 {index} 条非空源文本错误地输出空源标记")
        if any(not part.strip() for part in line.split(SPLIT_MARKER)):
            errors.append(f"第 {index} 条拆句译文包含空分段：ordinal={record['ordinal']}")
        if record.get("kind") == "menu" and SPLIT_MARKER in line:
            errors.append(f"第 {index} 条 menu 不能用 {SPLIT_MARKER} 拆成多段：ordinal={record['ordinal']}")
        if record.get("source") and line != EMPTY_SOURCE_MARKER:
            errors.extend(
                f"第 {index} 条 ordinal={record['ordinal']}：{error}"
                for error in _protected_content_errors(
                    record["source"],
                    line,
                    allow_paragraph_split=record.get("kind") == "dialogue",
                )
            )
        validated.append(line.strip())
    if errors:
        raise ValueError("翻译协议校验失败：\n" + "\n".join(errors))
    return validated


def request_response(endpoint: str, api_key: str, model: str, prompt: str, max_output_tokens: int, effort: str) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "instructions": INSTRUCTIONS,
        "input": prompt,
        "max_output_tokens": max_output_tokens,
        "store": False,
    }
    if effort != "default":
        payload["reasoning"] = {"effort": effort}
    request = Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=1800) as response:
            body = response.read()
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Responses API HTTP {error.code}: {details}") from error
    except URLError as error:
        raise RuntimeError(f"无法连接 Responses API：{error}") from error
    try:
        value = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as error:
        raise RuntimeError("Responses API 返回的不是 JSON") from error
    if not isinstance(value, dict):
        raise RuntimeError("Responses API 返回的 JSON 不是对象")
    if value.get("error"):
        raise RuntimeError(f"Responses API 返回错误：{value['error']}")
    return value


def translate_command(args: argparse.Namespace) -> int:
    records = read_jsonl(args.records)
    audit_records = read_jsonl(args.context_audit)
    audits = {int(record["ordinal"]): record for record in audit_records}
    missing = [record["ordinal"] for record in records if int(record["ordinal"]) not in audits]
    if missing:
        raise ValueError(f"context audit 缺少 ordinal：{missing}")
    if not records:
        raise ValueError("翻译批次为空")

    api_key = args.api_key or os.environ.get("OUTLAND_SUB2API_API_KEY")
    if not api_key:
        raise ValueError("请通过 --api-key 或 OUTLAND_SUB2API_API_KEY 提供本地 API key")

    args.output.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(records, audits)
    (args.output / "request.prompt.txt").write_text(prompt, encoding="utf-8", newline="\n")
    response = request_response(args.endpoint, api_key, args.model, prompt, args.max_output_tokens, args.reasoning_effort)
    (args.output / "response.json").write_text(
        json.dumps(response, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    text = response_text(response)
    (args.output / "output.raw.txt").write_text(text, encoding="utf-8", newline="\n")
    translations = validate_lines(text, records)
    with (args.output / "translations.tsv").open("w", encoding="utf-8", newline="\n") as handle:
        for record, translation in zip(records, translations):
            handle.write(f"{record['ordinal']}\t{translation}\n")
    usage = response.get("usage") if isinstance(response.get("usage"), dict) else {}
    metadata = {
        "records": len(records),
        "model": args.model,
        "endpoint": args.endpoint,
        "reasoning_effort": args.reasoning_effort,
        "output_lines": len(translations),
        "usage": usage,
        "status": response.get("status"),
    }
    (args.output / "result.meta.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(metadata, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records", type=Path, required=True, help="选定批次的 Record JSONL")
    parser.add_argument("--context-audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-key")
    parser.add_argument("--max-output-tokens", type=int, default=16000)
    parser.add_argument("--reasoning-effort", choices=("default", "low", "medium", "high"), default="medium")
    parser.set_defaults(function=translate_command)
    return parser


if __name__ == "__main__":
    try:
        arguments = build_parser().parse_args()
        raise SystemExit(arguments.function(arguments))
    except (RuntimeError, ValueError) as error:
        print(f"错误：{error}", file=sys.stderr)
        raise SystemExit(1)
