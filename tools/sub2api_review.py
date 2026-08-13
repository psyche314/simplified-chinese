"""Review translation changes from a Git commit through the local sub2api.

The input is reconstructed from the parent and commit snapshots, so this
driver does not depend on a checked-in/generated diff JSONL file.  It sends
translation candidates together with stable IDs, speaker information,
neighboring Ren'Py text, and the project's localization rules.  Requests are
bounded to six concurrent workers and successful batches can be reused after
an interrupted run.

After all batches finish, choices 1/2/3 are applied to the current working
tree: old translation, new translation, or model replacement respectively.
Choice 4 is never applied and is written to ``pending.jsonl``.  Use
``--review-only`` to produce the report without editing the package, or
``--prepare-only`` to validate extraction and prompt generation without any
network request.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Keep the project glossary in one place with the translation driver.  This
# import has no network or filesystem side effects.
TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from sub2api_translate import DEFAULT_ENDPOINT, DEFAULT_MODEL, PROJECT_GLOSSARY  # noqa: E402
from sub2api_apply import render_dialogue, replace_statement  # noqa: E402
from translation_batches import stable_menu_id  # noqa: E402


MAX_CONCURRENCY = 6
REPO_ROOT = Path(__file__).resolve().parents[1]
SPLIT_MARKER = "␟"
EMPTY_MARKER = "␀"
DEFAULT_LANGUAGE = "schinese_rewrite"
DEFAULT_PACKAGE = "game/tl/schinese_rewrite"

TRANSLATE_HEADER = re.compile(r"^translate\s+(?P<language>\S+)\s+(?P<key>.+):\s*$")
STRING_START = re.compile(r"(?<![A-Za-z0-9_])(?P<prefix>[rRuUbBfF]{0,2})(?P<quote>\"\"\"|'''|\"|')")
STRING_ENTRY = re.compile(r"^(?P<kind>old|new)\b")
IDENTIFIER_PREFIX = re.compile(r"^[A-Za-z_]\w*(?:\s+[A-Za-z_]\w*)*$")
PERCENT_TOKEN = re.compile(
    r"(?<!\d)%(?:%|\([^)]*\)|[0-9]+\$)?[-+#0 ]*(?:[0-9]+|\*)?(?:\.[0-9]+|\.\*)?[hlL]?[A-Za-z]"
)


REVIEW_INSTRUCTIONS = """你是《Outland Wanderer》的简体中文本地化审校员。你会收到一批来自同一个 Git 提交的翻译变更对象。每个对象都包含 source（开发者英文原文）、old_translation（提交前译文）和 new_translation（提交后译文），并附带稳定 ID、文件、说话者、相邻文本、文本类型和项目术语等上下文。

你的任务不是默认支持新译，也不是默认支持旧译，而是逐条以 source 为事实来源，结合完整上下文，严格在四个选项中选择：
1 = 旧翻译更好；2 = 新翻译更好；3 = 新旧翻译都不好，需要重新翻译，并给出 replacement；4 = 需要更多背景信息，现有信息不足以判断。

【审校优先级】
1. Ren'Py 结构和所有受保护 token 必须正确：方括号插值（包括嵌套表达式）、花括号文本标签及参数、百分号占位符、反斜杠转义和变量表达式必须逐项保留，不能改名、删减、增加或破坏嵌套关系。
2. source 是本条唯一事实来源。人物、地点、物品、关系、事件、动作、结果、否定、数量、条件、因果、时间、程度和信息完整性优先于文采。old_translation 可能错，new_translation 也可能错。
3. 中文自然度、语序、指代、角色声音和语体同样要审查。允许重排、拆句、合句和不改变事实的自然增译；不得创造 source 未暗示的新事件、原因、地点、人物、动机或状态，也不得擅自强化/减弱因果和程度。
4. 语体必须看局部背景：普通对白可以口语化，亲密或情绪化对白可以更口语；药草志、编年史、公告、仪式、正式说明、记录和庄重人物可使用书面语。不要把所有文本统一成口语，也不要把中世纪/西幻背景机械地套成古雅腔。角色的粗鲁、庄重、幼稚、讥讽、傲慢、怯懦等差异必须保留。
5. dialogue/旁白应自然、有节奏；menu/UI 应短、清楚、可扫描；成人、暴力、粗俗内容保持 source 的明确程度和强度，不洗掉关键动作，也不额外情色化或血腥化。
6. 项目术语要一致，但术语必须服从当前 source 和语境。完整复合术语优先于组成短词。若上下文明确说明大写词是人物名、专名或实体，不要误当普通词；反之也不要仅凭首字母大写就强行当人名。

【重要判断原则】
- 旧译和新译都要独立对照 source 审查；“新译改得更多”不等于更好，“旧译更顺”也不等于事实正确。
- 只有一方存在实质问题时，选择另一方；若两方都存在事实、格式、明显语病、严重直译腔或上下文错误，必须选择 3，并给出完整、自然、忠实的 replacement。
- 选 4 只用于当前对象确实缺少决定所必需的说话者、指代对象、专名含义、场景规则或代码语义；不要把它当作不愿判断的兜底。相邻文本和项目术语已经提供的信息不能再次声称缺失。
- 如果 old_translation 和 new_translation 都合格且没有明确优势，选择更自然、与局部语体更一致的一方；若两者确实同等合格，选择 1 或 2 中更符合上下文的一方，不要滥用 4。
- 不要因为数字从阿拉伯数字变成中文数字、或因为“HP damage”在中文中简化为“点伤害”就误报事实遗漏；应检查实际数量和游戏语义。

【项目背景】
这是一个带有成人内容的西幻/中世纪风格 Ren'Py RPG。世界观背景只影响有依据的语体和专名，不会让所有对白自动变成古风。玩家在莫肯大陆旅行，与山羊部落、熊族、狼人、精灵缚者、符文守护者等人物和实体互动；战斗文本、菜单、道具说明、剧情对白和书面记录的写法不同。上下文中的“neighbor”是相邻原文与译文，仅用于判断指代、说话者、术语和语气，不是新的待审对象。

【项目专属术语】
以下术语来自项目代码和既有翻译规范。出现明确对应英文时优先采用指定译法；说明用于消歧，不要把说明本身增译进没有该语义的句子：
""" + "\n".join(
    f"- {source} → {target}：{note}" for source, target, note in PROJECT_GLOSSARY
) + """

【校准范例】
范例只说明判断原则，不是固定模板：

英文：The Rune Guardian aims and flings 3 huge stones at you, it ignores your dodges and hit you right onto your body. Your health decreases by [ed] HP.
较差：符文守护者瞄准你，掷来三块巨石。巨石无视你的闪避，正面砸中你的身体。你的生命值减少了[ed]点。
较好：符文守护者瞄准你，投来三块巨石。你试图闪躲，却仍被巨石正面砸中。你的生命值减少了[ed]点。
原则：普通战斗旁白中“投来”比刻意书面的“掷来”自然；不要把“失败的闪避”机械写成巨石“无视闪避”。

英文：I should be honest with you, Lothar. I was not there... when it happened.
可能更好：我该跟你说实话，洛萨尔。事情发生的时候……我不在场。
原则：这里是情绪化对白，口语表达更合适；正式说明或庄重人物则应按背景使用书面语，不能套用“对白一律口语化”。

英文：As you search around the werewolf, you found an Iron ore, a Pelt and [exp_drop] EXP!
正确方向：你在狼人身边搜寻时，发现了铁矿石、毛皮和[exp_drop]点经验！
原则：iron ore 是未冶炼的“铁矿石”，不能因为代码奖励或上下文猜成“铁锭”；插值必须原样保留。

英文：feral werewolf
项目译法：狂化狼人
原则：这是项目实体术语；不要在同一批次中漂移成“野性狼人”“野蛮狼人”或“野生狼人”。

【输出协议】
严格只输出 JSONL，每个输入对象恰好一行，顺序完全一致。不要输出 Markdown 围栏、标题、编号、解释、确认词或空行。每行必须是以下对象：
{"ordinal":整数,"choice":1,"reason":"不超过80个汉字的关键理由"}
choice=1 或 2 时只能包含对应判断和 reason，不要给 replacement。
choice=3 时必须包含非空的 replacement，replacement 是完整重译文本，不带引号、Ren'Py 代码或解释；如果需要把一个 source 拆成多条相邻 Ren'Py 字符串，在同一 JSON 字符串中使用字符 ␟，不要使用物理换行。
choice=4 时必须包含非空的 missing_context，明确指出缺少什么背景；不得用空泛的“需要更多上下文”。
JSON 字符串中的换行必须合法转义。replacement 必须保留 source 的所有方括号、花括号、百分号和反斜杠 token。
"""


@dataclass(frozen=True)
class Entry:
    file: str
    language: str
    key: str
    occurrence: int
    kind: str
    speaker: str
    source: str
    translation: str

    @property
    def stable_id(self) -> str:
        if self.kind == "menu":
            return stable_menu_id(self.file, self.source, self.occurrence)
        suffix = "" if self.occurrence == 0 else f"#{self.occurrence + 1}"
        return f"{self.file}:{self.language}:{self.key}{suffix}"


@dataclass(frozen=True)
class ReviewRecord:
    ordinal: int
    file: str
    stable_id: str
    key: str
    occurrence: int
    kind: str
    speaker: str
    source: str
    old_translation: str
    new_translation: str
    context_before: tuple[dict[str, str], ...]
    context_after: tuple[dict[str, str], ...]
    glossary: tuple[dict[str, str], ...]

    def as_prompt_object(self) -> dict[str, Any]:
        return {
            "ordinal": self.ordinal,
            "file": self.file,
            "stable_id": self.stable_id,
            "translation_key": self.key,
            "occurrence": self.occurrence,
            "kind": self.kind,
            "speaker": self.speaker or None,
            "source": self.source,
            "old_translation": self.old_translation,
            "new_translation": self.new_translation,
            "context_before": list(self.context_before),
            "context_after": list(self.context_after),
            "relevant_project_glossary": list(self.glossary),
        }


@dataclass(frozen=True)
class Batch:
    number: int
    records: tuple[ReviewRecord, ...]


def run_git(*arguments: str, input_bytes: bytes | None = None) -> bytes:
    command = ["git", *arguments]
    result = subprocess.run(
        command,
        cwd=REPO_ROOT,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        details = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"Git 命令失败（{' '.join(command)}）：{details}")
    return result.stdout


def resolve_commit(commit: str) -> str:
    return run_git("rev-parse", "--verify", f"{commit}^{{commit}}").decode().strip()


def parent_commit(commit: str) -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", f"{commit}^1"],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        return None
    return result.stdout.decode("utf-8", errors="strict").strip()


def snapshot_text(commit: str | None, path: str) -> str:
    if commit is None:
        return ""
    result = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        # A changed file may have been added or deleted in the commit.  A
        # missing side is represented by an empty snapshot; other Git errors
        # remain actionable instead of being silently treated as empty.
        details = result.stderr.decode("utf-8", errors="replace")
        if "does not exist" in details or "exists on disk, but not in" in details:
            return ""
        raise RuntimeError(f"无法读取 Git 文件快照 {commit}:{path}：{details.strip()}")
    return result.stdout.decode("utf-8-sig")


def changed_package_files(commit: str, parent: str | None, package: str) -> list[str]:
    if parent is None:
        raw = run_git("ls-tree", "-r", "--name-only", commit, "--", package)
        candidates = raw.decode("utf-8", errors="strict").splitlines()
    else:
        raw = run_git("diff", "--name-only", parent, commit, "--", package)
        candidates = raw.decode("utf-8", errors="strict").splitlines()
    prefix = package.rstrip("/") + "/"
    return sorted(
        path for path in candidates if path.startswith(prefix) and path.endswith(".rpy")
    )


def closing_quote(text: str, start: int, quote: str) -> int | None:
    position = start + len(quote)
    while position < len(text):
        if text.startswith(quote, position):
            backslashes = 0
            previous = position - 1
            while previous >= 0 and text[previous] == "\\":
                backslashes += 1
                previous -= 1
            if backslashes % 2 == 0:
                return position
        position += 1
    return None


def find_string_literal(text: str) -> tuple[str, str, int] | None:
    for match in STRING_START.finditer(text):
        quote = match.group("quote")
        end = closing_quote(text, match.start("quote"), quote)
        if end is None:
            continue
        raw = text[match.start() : end + len(quote)]
        try:
            value = ast.literal_eval(raw)
        except (SyntaxError, ValueError):
            continue
        if isinstance(value, str):
            return value, raw, end + len(quote)
    return None


def consume_statement(lines: list[str], start: int) -> tuple[str, int] | None:
    statement = ""
    for index in range(start, len(lines)):
        if statement:
            statement += "\n"
        statement += lines[index]
        parsed = find_string_literal(statement)
        if parsed is not None:
            return parsed[0], index + 1
    return None


def split_blocks(text: str) -> list[tuple[str, str, list[str]]]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    starts = [index for index, line in enumerate(lines) if line.startswith("translate ")]
    blocks: list[tuple[str, str, list[str]]] = []
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        match = TRANSLATE_HEADER.fullmatch(lines[start])
        if match:
            blocks.append((match.group("language"), match.group("key"), lines[start:end]))
    return blocks


def source_comment(block: list[str]) -> tuple[str, str] | None:
    for line in block[1:]:
        stripped = line.lstrip()
        if not stripped.startswith("#"):
            continue
        comment = stripped[1:].lstrip()
        parsed = find_string_literal(comment)
        if parsed is None:
            continue
        source, raw, _ = parsed
        prefix = comment[: comment.find(raw)].strip()
        speaker = prefix.split()[0] if prefix else ""
        return speaker, source
    return None


def likely_translation_statement(line: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or stripped == "pass":
        return False
    if stripped.startswith(("if ", "elif ", "else:", "python:", "return ", "jump ", "call ")):
        return False
    parsed = find_string_literal(line)
    if parsed is None:
        return False
    prefix = line[: line.find(parsed[1])].strip()
    return not prefix or bool(IDENTIFIER_PREFIX.fullmatch(prefix))


def parse_dialogue_block(file: str, language: str, key: str, block: list[str], occurrence: int) -> Entry | None:
    source_info = source_comment(block)
    if source_info is None or key == "strings" or key.startswith("style "):
        return None
    speaker, source = source_info
    values: list[str] = []
    index = 1
    while index < len(block):
        if not likely_translation_statement(block[index]):
            index += 1
            continue
        parsed = consume_statement(block, index)
        if parsed is None:
            index += 1
            continue
        value, next_index = parsed
        values.append(value)
        index = next_index
    # Keep a source block even when one side is ``pass`` or otherwise has no
    # translated string.  Equal empty blocks are filtered after comparing the
    # parent and commit, while a pass-to-text/text-to-pass change must remain
    # reviewable.
    return Entry(file, language, key, occurrence, "dialogue", speaker, source, SPLIT_MARKER.join(values))


def parse_menu_blocks(file: str, language: str, key: str, block: list[str]) -> list[Entry]:
    if key != "strings":
        return []
    entries: list[Entry] = []
    pending_old: str | None = None
    occurrences: Counter[str] = Counter()
    index = 1
    while index < len(block):
        stripped = block[index].strip()
        match = STRING_ENTRY.match(stripped)
        if match is None:
            index += 1
            continue
        parsed = consume_statement(block, index)
        if parsed is None:
            raise ValueError(f"无法解析 strings 块：{file}:{key}:{index + 1}")
        value, next_index = parsed
        if match.group("kind") == "old":
            if pending_old is not None:
                raise ValueError(f"strings old 未配对：{file}:{index + 1}")
            pending_old = value
        else:
            if pending_old is None:
                raise ValueError(f"strings new 缺少 old：{file}:{index + 1}")
            occurrence = occurrences[pending_old]
            occurrences[pending_old] += 1
            entries.append(Entry(file, language, pending_old, occurrence, "menu", "", pending_old, value))
            pending_old = None
        index = next_index
    if pending_old is not None:
        raise ValueError(f"strings old 缺少 new：{file}")
    return entries


def parse_snapshot(file: str, text: str, language: str) -> list[Entry]:
    entries: list[Entry] = []
    dialogue_occurrences: Counter[str] = Counter()
    for block_language, key, block in split_blocks(text):
        if block_language != language:
            continue
        if key == "strings":
            entries.extend(parse_menu_blocks(file, block_language, key, block))
            continue
        occurrence = dialogue_occurrences[key]
        dialogue_occurrences[key] += 1
        entry = parse_dialogue_block(file, block_language, key, block, occurrence)
        if entry is not None:
            entries.append(entry)
    return entries


def entry_key(entry: Entry) -> tuple[str, str, int]:
    return entry.kind, entry.key, entry.occurrence


def glossary_matches(text: str) -> tuple[dict[str, str], ...]:
    normalized = text.replace("’", "'").lower()
    matches: list[dict[str, str]] = []
    for source, target, note in PROJECT_GLOSSARY:
        pattern = rf"(?<![A-Za-z]){re.escape(source.lower())}(?![A-Za-z])"
        if re.search(pattern, normalized):
            matches.append({"source": source, "target": target, "note": note})
    matches.sort(key=lambda item: len(item["source"]), reverse=True)
    return tuple(matches)


def context_item(entry: Entry) -> dict[str, str]:
    return {
        "stable_id": entry.stable_id,
        "speaker": entry.speaker,
        "source": entry.source,
        "translation": entry.translation,
    }


def build_review_records(
    commit: str,
    parent: str | None,
    files: list[str],
    language: str,
    neighbor_count: int,
) -> list[ReviewRecord]:
    records: list[ReviewRecord] = []
    for file in files:
        old_entries = parse_snapshot(file, snapshot_text(parent, file), language)
        new_entries = parse_snapshot(file, snapshot_text(commit, file), language)
        old_map = {entry_key(entry): entry for entry in old_entries}
        new_map = {entry_key(entry): entry for entry in new_entries}
        ordered_keys = list(dict.fromkeys([entry_key(entry) for entry in new_entries] + [entry_key(entry) for entry in old_entries]))
        context_entries = new_entries or old_entries
        context_positions = {entry_key(entry): index for index, entry in enumerate(context_entries)}

        for key in ordered_keys:
            old_entry = old_map.get(key)
            new_entry = new_map.get(key)
            source = (new_entry or old_entry).source  # type: ignore[union-attr]
            old_translation = old_entry.translation if old_entry else ""
            new_translation = new_entry.translation if new_entry else ""
            if old_entry is not None and new_entry is not None and source == old_entry.source and old_translation == new_translation:
                continue
            current = new_entry or old_entry
            if current is None:
                continue
            position = context_positions.get(key)
            if position is None:
                neighbors_before: list[dict[str, str]] = []
                neighbors_after: list[dict[str, str]] = []
            else:
                neighbors_before = [
                    context_item(item)
                    for item in context_entries[max(0, position - neighbor_count) : position]
                ]
                neighbors_after = [
                    context_item(item)
                    for item in context_entries[position + 1 : position + 1 + neighbor_count]
                ]
            combined = "\n".join(
                [source, old_translation, new_translation]
                + [item["source"] for item in neighbors_before + neighbors_after]
            )
            records.append(
                ReviewRecord(
                    ordinal=0,
                    file=file,
                    stable_id=current.stable_id,
                    key=current.key,
                    occurrence=current.occurrence,
                    kind=current.kind,
                    speaker=current.speaker,
                    source=source,
                    old_translation=old_translation,
                    new_translation=new_translation,
                    context_before=tuple(neighbors_before),
                    context_after=tuple(neighbors_after),
                    glossary=glossary_matches(combined),
                )
            )
    records.sort(key=lambda record: (record.file, record.stable_id))
    return [
        ReviewRecord(
            ordinal=index,
            file=record.file,
            stable_id=record.stable_id,
            key=record.key,
            occurrence=record.occurrence,
            kind=record.kind,
            speaker=record.speaker,
            source=record.source,
            old_translation=record.old_translation,
            new_translation=record.new_translation,
            context_before=record.context_before,
            context_after=record.context_after,
            glossary=record.glossary,
        )
        for index, record in enumerate(records, 1)
    ]


def jsonl_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"JSONL 第 {line_number} 行无效：{error}") from error
        if not isinstance(value, dict):
            raise ValueError(f"JSONL 第 {line_number} 行不是对象")
        records.append(value)
    return records


def batch_prompt(batch: Batch, total_records: int, commit: str, parent: str | None) -> str:
    files = sorted({record.file for record in batch.records})
    speakers = sorted({record.speaker for record in batch.records if record.speaker})
    context = {
        "commit": commit,
        "parent_commit": parent,
        "files_in_batch": files,
        "speakers_in_batch": speakers,
        "batch_number": batch.number,
        "batch_size": len(batch.records),
        "total_records": total_records,
    }
    lines = [
        "【本批次通用上下文】",
        json.dumps(context, ensure_ascii=False, separators=(",", ":")),
        "以下 JSONL 对象是审校输入。每个对象的 context_before/context_after 是同一文件中相邻的原文和当前译文，只用于理解省略、指代、说话者和语气；它们不是待审对象，也不能改变 source 的事实边界。relevant_project_glossary 是项目消歧资料，不是额外译文。",
        "重复 source 或重复稳定 ID 的对象仍要逐行审查。old_translation 是提交前文本，new_translation 是提交后文本；不要默认哪一方正确。",
        f"本批次对象数固定为 {len(batch.records)}，全局对象总数为 {total_records}。",
        "",
        "【审校对象 JSONL】",
    ]
    lines.extend(json.dumps(record.as_prompt_object(), ensure_ascii=False, separators=(",", ":")) for record in batch.records)
    lines.extend(
        [
            "",
            "【输出】",
            f"严格输出 {len(batch.records)} 行 JSONL，按 ordinal 顺序排列；每个对象只能对应一个输入对象。",
        ]
    )
    return "\n".join(lines)


def response_text(response: dict[str, Any]) -> str:
    pieces: list[str] = []
    for output in response.get("output", []):
        if not isinstance(output, dict):
            continue
        for content in output.get("content", []):
            if isinstance(content, dict) and content.get("type") == "output_text":
                value = content.get("text")
                if isinstance(value, str):
                    pieces.append(value)
    if pieces:
        return "\n".join(pieces)
    top_level = response.get("output_text")
    if isinstance(top_level, str) and top_level:
        return top_level
    raise ValueError("Responses API 没有返回 output_text")


def request_response(
    endpoint: str,
    api_key: str,
    model: str,
    prompt: str,
    max_output_tokens: int,
    reasoning_effort: str,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "instructions": REVIEW_INSTRUCTIONS,
        "input": prompt,
        "max_output_tokens": max_output_tokens,
        "store": False,
    }
    if reasoning_effort != "default":
        payload["reasoning"] = {"effort": reasoning_effort}
    request = Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
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


def protected_tokens(text: str) -> dict[str, Counter[str]]:
    def balanced(opening: str, closing: str) -> list[str]:
        values: list[str] = []
        depth = 0
        start = -1
        for index, character in enumerate(text):
            if character == opening:
                if depth == 0:
                    start = index
                depth += 1
            elif character == closing and depth:
                depth -= 1
                if depth == 0:
                    values.append(text[start : index + 1])
        return values

    return {
        "brackets": Counter(balanced("[", "]")),
        "tags": Counter(balanced("{", "}")),
        "percent": Counter(PERCENT_TOKEN.findall(text)),
        "escapes": Counter(re.findall(r"\\(?:.|$)", text, re.DOTALL)),
    }


def validate_replacement(source: str, replacement: str, *, kind: str = "dialogue") -> list[str]:
    if not replacement.strip():
        return ["replacement 为空"]
    if replacement == EMPTY_MARKER and source != "":
        return ["非空 source 不能使用空源标记"]
    if kind == "menu" and SPLIT_MARKER in replacement:
        return ["menu replacement 不能使用拆句分隔符"]
    source_tokens = protected_tokens(source)
    has_split = SPLIT_MARKER in replacement
    replacement_tokens = protected_tokens(replacement.replace(SPLIT_MARKER, ""))
    if has_split:
        # The translation writer may turn a source paragraph separator into
        # adjacent Ren'Py strings.  The separator itself is represented by
        # SPLIT_MARKER in the one-line review protocol.
        source_tokens["escapes"].pop(r"\n", None)
        replacement_tokens["escapes"].pop(r"\n", None)
    errors: list[str] = []
    for name in source_tokens:
        if source_tokens[name] != replacement_tokens[name]:
            errors.append(f"{name} token 不一致")
    if source.count("%") != replacement.count("%"):
        errors.append("百分号数量不一致")
    return errors


def parse_model_jsonl(raw: str, batch: Batch) -> list[dict[str, Any]]:
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    if lines and lines[0] == "```json":
        lines = lines[1:]
    if lines and lines[-1] == "```":
        lines = lines[:-1]
    expected = {record.ordinal: record for record in batch.records}
    parsed: list[dict[str, Any]] = []
    seen: set[int] = set()
    for line_number, line in enumerate(lines, 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"batch-{batch.number:04d} 输出第 {line_number} 行不是 JSON：{error}") from error
        if not isinstance(value, dict):
            raise ValueError(f"batch-{batch.number:04d} 输出第 {line_number} 行不是对象")
        ordinal = value.get("ordinal")
        if not isinstance(ordinal, int) or ordinal not in expected:
            raise ValueError(f"batch-{batch.number:04d} 返回了未知 ordinal：{ordinal!r}")
        if ordinal in seen:
            raise ValueError(f"batch-{batch.number:04d} 重复返回 ordinal：{ordinal}")
        seen.add(ordinal)
        choice = value.get("choice")
        if choice not in {1, 2, 3, 4}:
            raise ValueError(f"ordinal={ordinal} 的 choice 必须是 1、2、3 或 4")
        reason = value.get("reason")
        if not isinstance(reason, str) or not reason.strip() or "\n" in reason:
            raise ValueError(f"ordinal={ordinal} 的 reason 无效")
        normalized = {
            "ordinal": ordinal,
            "choice": choice,
            "reason": reason.strip(),
        }
        if choice == 3:
            replacement = value.get("replacement")
            if not isinstance(replacement, str):
                raise ValueError(f"ordinal={ordinal} 选择 3 却没有 replacement")
            errors = validate_replacement(
                expected[ordinal].source,
                replacement,
                kind=expected[ordinal].kind,
            )
            if errors:
                raise ValueError(f"ordinal={ordinal} 的 replacement 无效：{'；'.join(errors)}")
            normalized["replacement"] = replacement
        elif choice == 4:
            missing_context = value.get("missing_context")
            if not isinstance(missing_context, str) or not missing_context.strip():
                raise ValueError(f"ordinal={ordinal} 选择 4 却没有 missing_context")
            normalized["missing_context"] = missing_context.strip()
        parsed.append(normalized)
    if seen != set(expected):
        missing = sorted(set(expected) - seen)
        raise ValueError(f"batch-{batch.number:04d} 缺少 ordinal：{missing}")
    parsed.sort(key=lambda value: value["ordinal"])
    return parsed


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_jsonl(path: Path, values: Iterable[dict[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n" for value in values),
        encoding="utf-8",
        newline="\n",
    )


def batch_paths(output: Path, number: int) -> tuple[Path, Path, Path]:
    root = output / f"batch-{number:04d}"
    return root, root / "request.prompt.txt", root / "result.jsonl"


def run_one_batch(
    batch: Batch,
    output: Path,
    total_records: int,
    commit: str,
    parent: str | None,
    endpoint: str,
    model: str,
    api_key: str,
    max_output_tokens: int,
    reasoning_effort: str,
) -> dict[str, Any]:
    root, prompt_path, result_path = batch_paths(output, batch.number)
    root.mkdir(parents=True, exist_ok=True)
    prompt = batch_prompt(batch, total_records, commit, parent)
    prompt_sha256 = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    prompt_path.write_text(prompt, encoding="utf-8", newline="\n")
    response = request_response(endpoint, api_key, model, prompt, max_output_tokens, reasoning_effort)
    raw = response_text(response)
    (root / "response.json").write_text(json.dumps(response, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (root / "output.raw.txt").write_text(raw, encoding="utf-8", newline="\n")
    decisions = parse_model_jsonl(raw, batch)
    write_jsonl(result_path, decisions)
    metadata = {
        "batch": batch.number,
        "records": len(batch.records),
        "status": "completed",
        "commit": commit,
        "parent_commit": parent,
        "prompt_sha256": prompt_sha256,
        "usage": response.get("usage", {}),
        "model": model,
    }
    write_json(root / "result.meta.json", metadata)
    return metadata


def reusable_batch(
    output: Path,
    batch: Batch,
    total_records: int,
    commit: str,
    parent: str | None,
) -> list[dict[str, Any]] | None:
    _, _, result_path = batch_paths(output, batch.number)
    metadata_path = result_path.parent / "result.meta.json"
    if not result_path.is_file() or not metadata_path.is_file():
        return None
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        expected_prompt = batch_prompt(batch, total_records, commit, parent)
        expected_prompt_sha256 = hashlib.sha256(expected_prompt.encode("utf-8")).hexdigest()
        if (
            metadata.get("status") != "completed"
            or metadata.get("commit") != commit
            or metadata.get("parent_commit") != parent
            or metadata.get("batch") != batch.number
            or metadata.get("records") != len(batch.records)
            or metadata.get("prompt_sha256") != expected_prompt_sha256
        ):
            return None
        values = jsonl_records(result_path)
        parse_model_jsonl("\n".join(json.dumps(value, ensure_ascii=False) for value in values), batch)
        return values
    except (OSError, ValueError, json.JSONDecodeError):
        return None


def record_locator(record: ReviewRecord) -> tuple[str, str, str, int]:
    """Return the file-local location used by the current package renderer."""

    return record.file, record.kind, record.key, record.occurrence


def selected_translation(record: ReviewRecord, decision: dict[str, Any]) -> str | None:
    """Resolve a model choice to the exact text that should be written."""

    choice = decision["choice"]
    if choice == 1:
        return record.old_translation
    if choice == 2:
        return record.new_translation
    if choice == 3:
        return str(decision["replacement"])
    if choice == 4:
        return None
    raise ValueError(f"ordinal={record.ordinal} 的 choice 无效：{choice!r}")


def current_entries_by_locator(
    records: list[ReviewRecord],
    package: Path,
    language: str,
) -> tuple[dict[tuple[str, str, str, int], Entry], dict[str, str]]:
    """Read the working tree and verify it is still the reviewed commit.

    The model reviewed the commit snapshot, while applying edits the user may
    have changed the checkout.  Refuse to write if any reviewed source or new
    translation no longer matches; silently overwriting that work would make
    the review result unsafe.
    """

    files = sorted({record.file for record in records})
    entries: dict[tuple[str, str, str, int], Entry] = {}
    snapshots: dict[str, str] = {}
    conflicts: list[dict[str, Any]] = []
    for file in files:
        path = REPO_ROOT / file
        if not path.is_file() or not path.is_relative_to(package):
            conflicts.append({"file": file, "error": "工作区文件不存在或不在目标翻译目录内"})
            continue
        text = path.read_text(encoding="utf-8-sig")
        snapshots[file] = text
        for entry in parse_snapshot(file, text, language):
            locator = (file, entry.kind, entry.key, entry.occurrence)
            if locator in entries:
                conflicts.append({"file": file, "stable_id": entry.stable_id, "error": "当前工作区定位重复"})
            entries[locator] = entry

    for record in records:
        locator = record_locator(record)
        current = entries.get(locator)
        if current is None:
            conflicts.append({
                "ordinal": record.ordinal,
                "file": record.file,
                "stable_id": record.stable_id,
                "error": "当前工作区找不到审查对象",
            })
            continue
        if current.source != record.source:
            conflicts.append({
                "ordinal": record.ordinal,
                "file": record.file,
                "stable_id": record.stable_id,
                "error": "source 已改变",
                "review_source": record.source,
                "working_source": current.source,
            })
        if current.translation != record.new_translation:
            conflicts.append({
                "ordinal": record.ordinal,
                "file": record.file,
                "stable_id": record.stable_id,
                "error": "当前译文不是被审查的 new_translation",
                "review_new_translation": record.new_translation,
                "working_translation": current.translation,
            })
    if conflicts:
        raise RuntimeError(
            "工作区与审查提交不一致；为避免覆盖外部更改，未写入任何翻译。"
            f"冲突详情共 {len(conflicts)} 条。"
        )
    return entries, snapshots


def render_review_file(
    path: Path,
    replacements: dict[tuple[str, str, str, int], str],
    language: str,
) -> tuple[str, int]:
    """Apply selected replacements to one current-tree Ren'Py file."""

    file = path.relative_to(REPO_ROOT).as_posix()
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    starts = [index for index, line in enumerate(lines) if line.startswith("translate ")]
    dialogue_occurrences: Counter[str] = Counter()
    output: list[str] = []
    cursor = 0
    changed = 0

    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        block_lines = lines[start:end]
        match = TRANSLATE_HEADER.fullmatch(block_lines[0])
        rendered = block_lines
        if match is not None and match.group("language") == language:
            key = match.group("key")
            if key == "strings":
                menu_replacements: list[tuple[int, int, list[str]]] = []
                pending_old: str | None = None
                pending_old_occurrence: int | None = None
                menu_occurrences: Counter[str] = Counter()
                index = 1
                while index < len(block_lines):
                    stripped = block_lines[index].strip()
                    entry_match = STRING_ENTRY.match(stripped)
                    if entry_match is None:
                        index += 1
                        continue
                    parsed = consume_statement(block_lines, index)
                    if parsed is None:
                        raise ValueError(f"无法解析当前 strings 块：{file}:{index + 1}")
                    value, next_index = parsed
                    if entry_match.group("kind") == "old":
                        if pending_old is not None:
                            raise ValueError(f"当前 strings 块连续出现 old：{file}:{index + 1}")
                        pending_old = value
                        pending_old_occurrence = menu_occurrences[value]
                    else:
                        if pending_old is None or pending_old_occurrence is None:
                            raise ValueError(f"当前 strings new 缺少 old：{file}:{index + 1}")
                        locator = (file, "menu", pending_old, pending_old_occurrence)
                        replacement = replacements.get(locator)
                        if replacement is not None:
                            menu_replacements.append(
                                (
                                    index,
                                    next_index,
                                    replace_statement(block_lines, index, next_index, replacement),
                                )
                            )
                            changed += 1
                        menu_occurrences[pending_old] += 1
                        pending_old = None
                        pending_old_occurrence = None
                    index = next_index
                if pending_old is not None:
                    raise ValueError(f"当前 strings 块缺少 new：{file}")
                for block_start, block_end, replacement_lines in reversed(menu_replacements):
                    block_lines[block_start:block_end] = replacement_lines
                rendered = block_lines
            else:
                occurrence = dialogue_occurrences[key]
                dialogue_occurrences[key] += 1
                locator = (file, "dialogue", key, occurrence)
                replacement = replacements.get(locator)
                if replacement is not None and not key.startswith("style "):
                    rendered = render_dialogue(block_lines, replacement)
                    changed += 1

        output.extend(lines[cursor:start])
        output.extend(rendered)
        cursor = end
    output.extend(lines[cursor:])
    return "\n".join(output) + "\n", changed


def apply_review_results(
    args: argparse.Namespace,
    records: list[ReviewRecord],
    merged: list[dict[str, Any]],
) -> dict[str, Any]:
    """Apply choices 1/2/3 and record all choice-4 items for later work."""

    by_ordinal = {record.ordinal: record for record in records}
    decisions = {int(value["ordinal"]): value for value in merged}
    if set(decisions) != set(by_ordinal):
        raise RuntimeError("审查结果与审查对象数量不一致，拒绝写回")

    pending = [
        value
        for value in merged
        if value["choice"] == 4
    ]
    write_jsonl(args.output / "pending.jsonl", pending)

    replacements: dict[tuple[str, str, str, int], str] = {}
    action_counts = Counter[str]()
    for ordinal, record in by_ordinal.items():
        decision = decisions[ordinal]
        replacement = selected_translation(record, decision)
        if decision["choice"] == 4:
            action_counts["pending"] += 1
            continue
        if replacement is None:
            raise RuntimeError(f"ordinal={ordinal} 没有可应用的译文")
        errors = validate_replacement(record.source, replacement, kind=record.kind)
        if errors:
            raise RuntimeError(
                f"ordinal={ordinal} 选择的译文无法安全写回：{'；'.join(errors)}"
            )
        replacements[record_locator(record)] = replacement
        action_counts[{1: "old", 2: "new", 3: "replacement"}[decision["choice"]]] += 1

    package = (REPO_ROOT / args.package).resolve()
    if not package.is_dir() or not package.is_relative_to(REPO_ROOT):
        raise ValueError(f"目标翻译目录无效：{package}")
    _, snapshots = current_entries_by_locator(records, package, args.language)

    rendered_files: dict[Path, tuple[str, int]] = {}
    changed_files = 0
    changed_records = 0
    for file in sorted({record.file for record in records}):
        path = REPO_ROOT / file
        content, changed = render_review_file(path, {
            locator: value
            for locator, value in replacements.items()
            if locator[0] == file
        }, args.language)
        rendered_files[path] = (content, changed)
        changed_records += changed
        changed_files += changed > 0

    if not args.review_only:
        for path, original in snapshots.items():
            current = (REPO_ROOT / path).read_text(encoding="utf-8-sig")
            if current != original:
                raise RuntimeError(f"写回前工作区文件又发生变化，未写入：{path}")
        for path, (content, changed) in rendered_files.items():
            if changed and content != snapshots[path.relative_to(REPO_ROOT).as_posix()]:
                path.write_text(content, encoding="utf-8", newline="\n")

    metadata = {
        "status": "review-only" if args.review_only else "applied",
        "choice_1_old": action_counts["old"],
        "choice_2_new": action_counts["new"],
        "choice_3_replacement": action_counts["replacement"],
        "choice_4_pending": action_counts["pending"],
        "changed_records": changed_records,
        "changed_files": changed_files,
        "pending_file": str(args.output / "pending.jsonl"),
    }
    write_json(args.output / "apply.meta.json", metadata)
    return metadata


def prepare_command(args: argparse.Namespace) -> tuple[str, str | None, list[ReviewRecord], list[Batch]]:
    commit = resolve_commit(args.commit)
    parent = parent_commit(commit)
    files = changed_package_files(commit, parent, args.package)
    if not files:
        raise ValueError(f"提交没有修改 {args.package} 下的 .rpy 文件")
    records = build_review_records(commit, parent, files, args.language, args.neighbors)
    if not records:
        raise ValueError("提交中的目标文件没有可审查的翻译变更")
    batches = tuple(
        Batch(number=index, records=tuple(records[start : start + args.batch_size]))
        for index, start in enumerate(range(0, len(records), args.batch_size), 1)
    )
    return commit, parent, records, list(batches)


def write_prepared(output: Path, commit: str, parent: str | None, records: list[ReviewRecord], batches: list[Batch]) -> None:
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "manifest.json", {
        "commit": commit,
        "parent_commit": parent,
        "records": len(records),
        "batches": len(batches),
        "max_concurrency": MAX_CONCURRENCY,
        "batch_sizes": [len(batch.records) for batch in batches],
    })
    write_jsonl(output / "records.jsonl", (record.as_prompt_object() for record in records))
    for batch in batches:
        root, prompt_path, _ = batch_paths(output, batch.number)
        root.mkdir(parents=True, exist_ok=True)
        prompt_path.write_text(batch_prompt(batch, len(records), commit, parent), encoding="utf-8", newline="\n")


def review_command(args: argparse.Namespace) -> int:
    if not 1 <= args.max_concurrency <= MAX_CONCURRENCY:
        raise ValueError(f"并发数必须在 1 到 {MAX_CONCURRENCY} 之间；脚本硬上限是 {MAX_CONCURRENCY}")
    if args.batch_size <= 0:
        raise ValueError("batch-size 必须为正数")
    if args.neighbors < 0:
        raise ValueError("neighbors 不能为负数")
    if args.retries < 0:
        raise ValueError("retries 不能为负数")
    commit, parent, records, batches = prepare_command(args)
    write_prepared(args.output, commit, parent, records, batches)
    print(json.dumps({"commit": commit, "parent_commit": parent, "records": len(records), "batches": len(batches)}, ensure_ascii=False))
    if args.prepare_only:
        return 0

    api_key = args.api_key or os.environ.get("OUTLAND_SUB2API_API_KEY")
    if not api_key:
        raise ValueError("请通过 --api-key 或 OUTLAND_SUB2API_API_KEY 提供本地 API key")

    decisions: dict[int, dict[str, Any]] = {}
    pending: list[Batch] = []
    for batch in batches:
        reused = (
            reusable_batch(args.output, batch, len(records), commit, parent)
            if args.resume
            else None
        )
        if reused is None:
            pending.append(batch)
        else:
            decisions.update({int(value["ordinal"]): value for value in reused})

    if pending:
        # The only parallel section is the actual API request.  The executor
        # is constructed with the validated hard cap and is never expanded by
        # retries or by the number of files in a batch.
        for retry_round in range(args.retries + 1):
            if not pending:
                break
            failed: list[Batch] = []
            with ThreadPoolExecutor(max_workers=args.max_concurrency) as executor:
                futures = {
                    executor.submit(
                        run_one_batch,
                        batch,
                        args.output,
                        len(records),
                        commit,
                        parent,
                        args.endpoint,
                        args.model,
                        api_key,
                        args.max_output_tokens,
                        args.reasoning_effort,
                    ): batch
                    for batch in pending
                }
                for future in as_completed(futures):
                    batch = futures[future]
                    try:
                        metadata = future.result()
                        result_path = batch_paths(args.output, batch.number)[2]
                        values = jsonl_records(result_path)
                        decisions.update({int(value["ordinal"]): value for value in values})
                        print(json.dumps({"batch": batch.number, "status": metadata["status"]}, ensure_ascii=False), flush=True)
                    except Exception as error:  # noqa: BLE001 - preserve batch failure and continue others
                        failed.append(batch)
                        batch_root = batch_paths(args.output, batch.number)[0]
                        write_json(batch_root / "error.json", {"error": str(error), "retry_round": retry_round})
                        print(json.dumps({"batch": batch.number, "status": "failed", "error": str(error)}, ensure_ascii=False), flush=True)
            pending = failed
        if pending:
            raise RuntimeError("仍有批次失败；未自动丢弃已完成结果：" + ", ".join(f"batch-{batch.number:04d}" for batch in pending))

    merged: list[dict[str, Any]] = []
    records_by_ordinal = {record.ordinal: record for record in records}
    for ordinal in range(1, len(records) + 1):
        if ordinal not in decisions:
            raise RuntimeError(f"缺少审查结果 ordinal={ordinal}")
        record = records_by_ordinal[ordinal]
        merged.append({
            "ordinal": ordinal,
            "file": record.file,
            "stable_id": record.stable_id,
            "kind": record.kind,
            "speaker": record.speaker,
            "translation_key": record.key,
            "occurrence": record.occurrence,
            "source": record.source,
            "old_translation": record.old_translation,
            "new_translation": record.new_translation,
            "context_before": list(record.context_before),
            "context_after": list(record.context_after),
            "relevant_project_glossary": list(record.glossary),
            **decisions[ordinal],
        })
    write_jsonl(args.output / "review.jsonl", merged)
    apply_metadata = apply_review_results(args, records, merged)
    write_json(args.output / "dispatch.meta.json", {
        "commit": commit,
        "parent_commit": parent,
        "records": len(records),
        "batches": len(batches),
        "max_concurrency": args.max_concurrency,
        "retries": args.retries,
        "endpoint": args.endpoint,
        "model": args.model,
        "status": "completed",
        "apply": apply_metadata,
    })
    print(json.dumps({
        "status": "reviewed-and-applied" if not args.review_only else "reviewed",
        "records": len(merged),
        "output": str(args.output / "review.jsonl"),
        "apply": apply_metadata,
    }, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True, help="要审查的 Git 提交哈希或可解析引用")
    parser.add_argument("--output", type=Path, default=Path("_staging/sub2api-review"), help="审查产物目录，默认写入被忽略的 _staging/sub2api-review")
    parser.add_argument("--package", default=DEFAULT_PACKAGE, help="提交中待审查的翻译目录")
    parser.add_argument("--language", default=DEFAULT_LANGUAGE)
    parser.add_argument("--batch-size", type=int, default=50, help="每个 API 请求包含的审查对象数")
    parser.add_argument("--neighbors", type=int, default=2, help="每条对象注入的前后相邻条目数")
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-key")
    parser.add_argument("--max-output-tokens", type=int, default=20000)
    parser.add_argument("--reasoning-effort", choices=("default", "low", "medium", "high"), default="high")
    parser.add_argument("--max-concurrency", type=int, default=MAX_CONCURRENCY, help=f"API 并发数，硬上限为 {MAX_CONCURRENCY}")
    parser.add_argument("--retries", type=int, default=0, help="失败批次的重试次数；默认 0，避免未经确认的重复计费")
    parser.add_argument("--no-resume", dest="resume", action="store_false", help="不复用输出目录中已验证的成功批次")
    parser.add_argument("--prepare-only", action="store_true", help="只从提交生成审查输入，不发起 API 请求")
    parser.add_argument("--review-only", action="store_true", help="只生成审查结果和 pending.jsonl，不修改翻译文件")
    parser.set_defaults(resume=True)
    return parser


if __name__ == "__main__":
    try:
        arguments = build_parser().parse_args()
        raise SystemExit(review_command(arguments))
    except (RuntimeError, ValueError) as error:
        print(f"错误：{error}", file=sys.stderr)
        raise SystemExit(1)
