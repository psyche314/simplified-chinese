"""Extract compact translation batches without exposing Ren'Py source files.

The extractor treats stable translation identifiers as the only dialogue
address.  It keeps the current language package as a structural template and
emits JSONL metadata plus a tab-separated, one-record-per-line prompt input
for translation agents.  Agent output can therefore be mapped back by order
without asking an agent to reproduce Ren'Py headers or code.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import warnings
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Optional


TRANSLATE_HEADER = re.compile(r"^translate\s+(?P<language>\S+)\s+(?P<key>.+):$")
STRING_START = re.compile(
    r"(?<![A-Za-z0-9_])(?P<prefix>[rRuUbBfF]{0,2})(?P<quote>\"\"\"|'''|\"|')"
)
SOURCE_LINE_NUMBER = re.compile(r"^\s*# game/.*:\d+\s*$")
STRING_ENTRY = re.compile(r"^(?P<kind>old|new)\b")
GENERATOR_HEADER = re.compile(
    r"^# (?:Generated from developer English by generate_rewrite_translation\.py\.|"
    r"Do not edit compiled source files to change this language package\.|"
    r"Generated from developer English menu strings\.)$"
)

SENSITIVE_WORDS = (
    "cock",
    "cum",
    "dick",
    "fuck",
    "sex",
    "lust",
    "naked",
    "pussy",
    "semen",
    "slut",
)
SPLIT_MARKER = "␟"
CONTEXT_WORDS = (
    "again",
    "another",
    "here",
    "he",
    "her",
    "him",
    "his",
    "it",
    "its",
    "she",
    "that",
    "they",
    "there",
    "this",
    "those",
    "you",
)
PRONOUN_WORDS = {
    "he",
    "her",
    "hers",
    "him",
    "his",
    "it",
    "its",
    "she",
    "they",
    "them",
    "their",
    "theirs",
    "we",
}
DEICTIC_WORDS = {
    "again",
    "another",
    "here",
    "there",
    "this",
    "that",
    "these",
    "those",
}
QUANTITY_WORDS = {
    "all",
    "both",
    "each",
    "few",
    "many",
    "more",
    "one",
    "once",
    "only",
    "several",
    "some",
    "two",
    "three",
    "every",
}
CONDITION_WORDS = {
    "although",
    "because",
    "before",
    "but",
    "else",
    "if",
    "unless",
    "until",
    "when",
    "while",
}
GENERIC_CHARACTER_NAMES = {
    "Book",
    "Crowd",
    "Crew",
    "Guard",
    "Patron",
    "Tutorial",
    "You",
    "",
}


@dataclass
class Record:
    """One translatable unit in stable, file-local order."""

    ordinal: int
    file: str
    id: str
    kind: str
    speaker: str
    source: str
    current: str
    current_parts: list[str]
    old_reference: Optional[str]
    context_before: Optional[str]
    context_after: Optional[str]
    source_statement: str


@dataclass
class Block:
    file: str
    key: str
    header: str
    lines: list[str]


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8-sig").splitlines()


def parse_blocks(path: Path, language: str) -> list[Block]:
    """Parse translation blocks while ignoring generated line-number comments."""

    lines = [line for line in read_lines(path) if not SOURCE_LINE_NUMBER.match(line)]
    starts = [index for index, line in enumerate(lines) if line.startswith("translate ")]
    blocks: list[Block] = []

    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        match = TRANSLATE_HEADER.fullmatch(lines[start])
        if not match:
            raise ValueError(f"无法解析翻译头：{path}:{start + 1}: {lines[start]!r}")
        if match.group("language") != language:
            continue
        blocks.append(
            Block(
                file=path.name,
                key=match.group("key"),
                header=lines[start],
                lines=lines[start:end],
            )
        )

    return blocks


def _closing_quote(text: str, start: int, quote: str) -> Optional[int]:
    """Find an unescaped closing quote, including for triple-quoted text."""

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


def find_string_literal(text: str) -> tuple[str, str, int]:
    """Return decoded value, raw literal, and end offset from source text.

    Ren'Py's generated strings translations can use ``_p(...)`` around a
    triple-quoted literal.  A line-oriented regular expression cannot parse
    those values, so this small scanner deliberately handles both ordinary
    and triple-quoted Python-compatible literals across physical lines.
    """

    for match in STRING_START.finditer(text):
        quote = match.group("quote")
        end = _closing_quote(text, match.start("quote"), quote)
        if end is None:
            continue
        raw = text[match.start(): end + len(quote)]
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                value = ast.literal_eval(raw)
        except (SyntaxError, ValueError) as error:
            raise ValueError(f"字符串字面量无法解析：{raw!r}") from error
        if not isinstance(value, str):
            raise ValueError(f"字符串字面量解析结果不是文本：{raw!r}")
        return value, raw, end + len(quote)
    raise ValueError(f"翻译语句没有完整的字符串字面量：{text!r}")


def first_string_literal(line: str) -> tuple[str, str]:
    """Return decoded value and its raw literal from a Ren'Py statement."""

    value, raw, _ = find_string_literal(line)
    return value, raw


def consume_string_statement(lines: list[str], start: int) -> tuple[str, int]:
    """Consume one old/new statement, returning its value and next line."""

    statement = ""
    for index in range(start, len(lines)):
        if statement:
            statement += "\n"
        statement += lines[index]
        try:
            value, _, _ = find_string_literal(statement)
        except ValueError:
            continue
        return value, index + 1
    raise ValueError(f"字符串语句未闭合：{lines[start:]!r}")


def source_comment(block: Block) -> tuple[str, str, str]:
    """Return speaker, decoded English source, and source statement."""

    comments = [
        line.strip()[1:].lstrip()
        for line in block.lines[1:]
        if line.startswith("    #") and not SOURCE_LINE_NUMBER.match(line)
    ]
    if len(comments) != 1:
        raise ValueError(
            f"普通翻译块必须有一条英文原文注释：{block.file}:{block.key}，实际 {len(comments)} 条"
        )

    statement = comments[0]
    try:
        source, raw, _ = find_string_literal(statement)
    except ValueError as error:
        raise ValueError(f"英文原文注释没有完整字符串字面量：{block.file}:{block.key}") from error
    literal_start = statement.find(raw)
    if literal_start < 0:
        raise ValueError(f"英文原文注释字面量定位失败：{block.file}:{block.key}")
    prefix = statement[:literal_start].strip()
    speaker = prefix.split()[0] if prefix else ""
    return speaker, source, statement


def dialogue_value(block: Block) -> str:
    return "".join(dialogue_parts(block))


def dialogue_parts(block: Block) -> list[str]:
    payload = [
        line.rstrip()
        for line in block.lines[1:]
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if not payload:
        raise ValueError(
            f"普通翻译块必须有译文语句：{block.file}:{block.key}，实际 {len(payload)} 条"
        )
    # Ren'Py permits adjacent quoted statements to form one translated
    # dialogue block.  The old package uses this for a handful of long
    # translations, so references are normalized to their concatenated text.
    return [first_string_literal(line)[0] for line in payload]


def string_pairs(block: Block) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    old: Optional[str] = None
    new: Optional[str] = None

    index = 1
    while index < len(block.lines):
        line = block.lines[index]
        if not line.strip():
            index += 1
            continue
        stripped = line.strip()
        if stripped.startswith("#"):
            index += 1
            continue
        entry = STRING_ENTRY.match(stripped)
        if entry is None:
            raise ValueError(f"未知 strings 条目：{block.file}:{block.key}: {line!r}")
        kind = entry.group("kind")
        value, next_index = consume_string_statement(block.lines, index)
        if kind == "old":
            if old is not None:
                raise ValueError(f"菜单 old 条目未闭合：{block.file}:{block.key}")
            old = value
        else:
            if old is None or new is not None:
                raise ValueError(f"菜单 new 条目顺序错误：{block.file}:{block.key}")
            new = value
            pairs.append((old, new))
            old = None
            new = None
        index = next_index

    if old is not None or new is not None:
        raise ValueError(f"菜单条目缺少 old/new：{block.file}:{block.key}")
    return pairs


def package_values(package: Path, language: str) -> tuple[dict[tuple[str, str], str], dict[tuple[str, str, int], str]]:
    """Read old dialogue and menu values for optional reference use."""

    dialogue: dict[tuple[str, str], str] = {}
    menus: dict[tuple[str, str, int], str] = {}
    occurrences: Counter[tuple[str, str]] = Counter()

    for path in sorted(package.glob("*.rpy")):
        for block in parse_blocks(path, language):
            if block.key == "strings":
                for old, new in string_pairs(block):
                    key = (path.name, old)
                    occurrence = occurrences[key]
                    occurrences[key] += 1
                    menus[(path.name, old, occurrence)] = new
            elif not block.key.startswith("style ") and block.key not in {"python", "early", "late"}:
                if any(line.strip() == "pass" for line in block.lines[1:]):
                    continue
                # Old language packages may use executable conditionals inside
                # a translation block.  Such blocks are valid Ren'Py, but
                # their code is not a safe single reference translation for
                # an agent prompt.  Adjacent quoted statements remain valid
                # and are concatenated by dialogue_value().
                try:
                    dialogue[(path.name, block.key)] = dialogue_value(block)
                except ValueError:
                    continue

    return dialogue, menus


def needs_context(source: str) -> bool:
    lowered = source.lower()
    words = set(re.findall(r"[a-z]+", lowered))
    return (
        len(source) <= 80
        or source.rstrip().endswith(("...", "…"))
        or bool(words & set(CONTEXT_WORDS))
    )


def has_protected_content(record: Record) -> bool:
    return any(marker in record.source for marker in ("[", "]", "{", "}", "%", "\\n"))


def is_sensitive(record: Record) -> bool:
    lowered = record.source.lower()
    return any(word in lowered for word in SENSITIVE_WORDS)


def stable_menu_id(file: str, source: str, occurrence: int) -> str:
    digest = hashlib.sha1(source.encode("utf-8")).hexdigest()[:12]
    suffix = "" if occurrence == 0 else f"_{occurrence + 1}"
    return f"{file}:strings:{digest}{suffix}"


def extract_records(package: Path, language: str, old_package: Optional[Path]) -> list[Record]:
    old_dialogue: dict[tuple[str, str], str] = {}
    old_menus: dict[tuple[str, str, int], str] = {}
    if old_package is not None:
        old_dialogue, old_menus = package_values(old_package, "schinese")

    records: list[Record] = []
    menu_occurrences: Counter[tuple[str, str]] = Counter()
    source_by_file: dict[str, list[str]] = defaultdict(list)
    pending: list[tuple[str, str, str, str, str, str, Optional[str], list[str]]] = []

    for path in sorted(package.glob("*.rpy")):
        for block in parse_blocks(path, language):
            if block.key.startswith("style "):
                continue
            if block.key in {"python", "early", "late"}:
                continue
            if block.key == "strings":
                for source, current in string_pairs(block):
                    occurrence_key = (path.name, source)
                    occurrence = menu_occurrences[occurrence_key]
                    menu_occurrences[occurrence_key] += 1
                    old_reference = old_menus.get((path.name, source, occurrence))
                    pending.append(
                        (
                            path.name,
                            stable_menu_id(path.name, source, occurrence),
                            "menu",
                            "",
                            source,
                            current,
                            old_reference,
                            [current],
                        )
                    )
                    source_by_file[path.name].append(source)
            else:
                speaker, source, statement = source_comment(block)
                current_parts = dialogue_parts(block)
                current = "".join(current_parts)
                pending.append(
                    (
                        path.name,
                        block.key,
                        "dialogue",
                        speaker,
                        source,
                        current,
                        old_dialogue.get((path.name, block.key)),
                        current_parts,
                    )
                )
                source_by_file[path.name].append(source)

    file_positions: dict[str, list[int]] = defaultdict(list)
    local_positions: dict[int, int] = {}
    for index, item in enumerate(pending):
        local_positions[index] = len(file_positions[item[0]])
        file_positions[item[0]].append(index)

    for ordinal, item in enumerate(pending, start=1):
        file_name, identifier, kind, speaker, source, current, old_reference, current_parts = item
        local_position = local_positions[ordinal - 1]
        before = None
        after = None
        if kind == "menu" or needs_context(source):
            if local_position > 0:
                before = source_by_file[file_name][local_position - 1]
            if local_position + 1 < len(source_by_file[file_name]):
                after = source_by_file[file_name][local_position + 1]

        records.append(
            Record(
                ordinal=ordinal,
                file=file_name,
                id=identifier,
                kind=kind,
                speaker=speaker,
                source=source,
                current=current,
                current_parts=current_parts,
                old_reference=old_reference,
                context_before=before,
                context_after=after,
                source_statement=(f"{speaker} {json.dumps(source, ensure_ascii=False)}" if speaker else json.dumps(source, ensure_ascii=False)),
            )
        )

    return records


def write_jsonl(path: Path, records: Iterable[Record]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(asdict(record), ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def read_jsonl(path: Path) -> list[Record]:
    records: list[Record] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(Record(**json.loads(line)))
        except (TypeError, ValueError, json.JSONDecodeError) as error:
            raise ValueError(f"无法读取 JSONL 第 {line_number} 行：{error}") from error
    return records


def escape_prompt_field(value: Optional[str]) -> str:
    if value is None:
        return "-"
    return (
        value.replace("\\", "\\\\")
        .replace("\r", "\\r")
        .replace("\n", "\\n")
        .replace("\t", "\\t")
        .replace(SPLIT_MARKER, "\\u241f")
    )


def prompt_lines(records: Iterable[Record]) -> list[str]:
    lines = []
    for record in records:
        lines.append(
            "\t".join(
                (
                    str(record.ordinal),
                    record.kind,
                    escape_prompt_field(record.speaker or "—"),
                    escape_prompt_field(record.source),
                    escape_prompt_field(record.old_reference),
                    escape_prompt_field(record.context_before),
                    escape_prompt_field(record.context_after),
                )
            )
        )
    return lines


def write_prompt(path: Path, records: Iterable[Record]) -> None:
    path.write_text("\n".join(prompt_lines(records)) + "\n", encoding="utf-8", newline="\n")


def evenly(records: list[Record], count: int) -> list[Record]:
    if count <= 0 or not records:
        return []
    if count >= len(records):
        return records[:]
    if count == 1:
        return [records[len(records) // 2]]
    indexes = {round(index * (len(records) - 1) / (count - 1)) for index in range(count)}
    return [records[index] for index in sorted(indexes)]


def choose_pilot(records: list[Record], count: int) -> list[Record]:
    """Select a deterministic, diverse calibration sample."""

    selected: dict[int, Record] = {}

    def add_category(candidates: list[Record], quota: int) -> None:
        for record in evenly(candidates, quota):
            selected[record.ordinal] = record

    add_category([record for record in records if record.kind == "menu"], min(25, count // 5))
    add_category([record for record in records if "battle" in record.id.lower()], min(30, count // 4))
    add_category([record for record in records if has_protected_content(record)], min(30, count // 4))
    add_category([record for record in records if len(record.source) <= 45], min(25, count // 5))
    add_category([record for record in records if record.old_reference], min(25, count // 5))
    add_category([record for record in records if is_sensitive(record)], min(20, count // 8))

    remaining = [record for record in records if record.ordinal not in selected]
    needed = max(0, count - len(selected))
    add_category(remaining, needed)
    return sorted(selected.values(), key=lambda record: record.ordinal)[:count]


def character_aliases(project_root: Path) -> dict[str, str]:
    """Read character aliases and their display names from game code."""

    game_root = project_root / "game"
    if not game_root.exists():
        return {}

    definitions: dict[str, tuple[Optional[str], Optional[str]]] = {}
    definition_pattern = re.compile(
        r"^\s*(?:define|default)\s+(?P<alias>[A-Za-z_]\w*)\s*=\s*"
        r"Character\((?P<arguments>.*)\)\s*$"
    )
    for path in sorted(game_root.rglob("*.rpy")):
        if "tl" in path.relative_to(game_root).parts:
            continue
        for line in read_lines(path):
            match = definition_pattern.match(line)
            if match is None:
                continue
            alias = match.group("alias")
            arguments = match.group("arguments")
            leading = arguments.lstrip()
            # A Character(kind=...) inherits its display name from another
            # alias.  Only inspect the leading name expression; otherwise a
            # later outline color such as "#000" would be mistaken for the
            # character's name.
            name = None
            if leading.startswith(("_", "u_", '"', "'", 'u"', "u'")):
                try:
                    name, _ = first_string_literal(leading)
                except ValueError:
                    name = None
            kind_match = re.search(r"\bkind\s*=\s*([A-Za-z_]\w*)", arguments)
            definitions[alias] = (name, kind_match.group(1) if kind_match else None)

    aliases: dict[str, str] = {}

    def resolve(alias: str, seen: set[str]) -> Optional[str]:
        if alias in aliases:
            return aliases[alias]
        if alias in seen or alias not in definitions:
            return None
        seen.add(alias)
        name, kind = definitions[alias]
        if name is None and kind is not None:
            name = resolve(kind, seen)
        if name is not None:
            aliases[alias] = name
        return name

    for alias in definitions:
        resolve(alias, set())
    return aliases


def matched_terms(source: str, terms: Iterable[str]) -> list[str]:
    """Return known English terms explicitly present in a source string."""

    matches = []
    for term in sorted(set(terms), key=lambda value: (-len(value), value.lower())):
        if len(term) < 3:
            continue
        pattern = rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])"
        if re.search(pattern, source, re.IGNORECASE):
            matches.append(term)
    return matches


def scene_family(record: Record) -> str:
    """Return a stable, compact scene family for batch-level context."""

    value = f"{record.file}:{record.id}".lower()
    if Path(record.file).stem.lower().startswith("book_pages"):
        return "lore-book"
    if record.kind == "menu":
        return f"menu:{Path(record.file).stem}"
    if "battle" in value or "lose" in value or "win" in value:
        return "battle"
    if "book" in value or "journal" in value:
        return "lore-book"
    if "shop" in value or "craft" in value:
        return "commerce-and-crafting"
    if "map" in value or "lusterfield" in value or "forest" in value:
        return "exploration"
    return Path(record.file).stem


_BOTANICAL_JOURNAL_IDS = {
    "book_pages.rpy:strings:14e1be8f39bf",
    "book_pages.rpy:strings:874d8cecbb31",
}


def translation_context(record: Record) -> tuple[str, str, Optional[str]]:
    """Describe the local text role, register, and narrowly relevant lore.

    Ren'Py ``strings`` blocks contain both UI labels and long runtime prose, so
    the structural ``kind`` alone cannot determine how a line should sound.
    These fields are prompt metadata only; they never become translated text.
    """

    stem = Path(record.file).stem.lower()
    value = f"{record.file}:{record.id}".lower()

    if record.id in _BOTANICAL_JOURNAL_IDS:
        return (
            "私人药草研究笔记（受损文本）",
            "采用清楚、略正式但仍带私人笔记口吻的药理记录体；专业内容要准确，文字损坏造成的断裂必须保留，不能猜补成完整事实。",
            "这是同一本私人植物与药理研究笔记中相邻的两页。Somni-Etern 是幻想蘑菇专名，固定译为“永恒梦魇”。原文中的连字符、破折号和残缺字母表现纸页或文字受损；中文应让读者感到信息缺损，而不是擅自复原作者原句。",
        )

    if stem.startswith("book_pages"):
        source_lower = record.source.lower()
        if "echinacea" in source_lower or "infection" in source_lower and "patient" in source_lower:
            return (
                "私人药草研究笔记",
                "采用清楚、略正式但仍带私人笔记口吻的药理记录体；兼顾专业信息和作者个人经历，不写成 UI 说明或古文。",
                "这是私人植物与药理研究笔记的一部分，作者既记录药效，也会写入个人判断和经历。",
            )
        return (
            "世界观书籍或编年文本",
            "采用符合书籍载体的连贯书面叙事；可有历史记录感，但不要机械套用古语、伪古文或现代网络表达。",
            "这是游戏内供玩家阅读的世界观文本；具体语感由本页主题和上下文决定，而不是由整个西幻世界观一概决定。",
        )

    if record.kind == "menu":
        return (
            "UI、菜单或运行时短文本",
            "简洁、直接、可扫描；优先表达功能，不扩写成叙事句，也不要为了西幻氛围强行古雅化。",
            None,
        )

    if record.speaker:
        if "battle" in value:
            return (
                "战斗中的角色对白",
                "保持说话者身份、情绪和粗俗程度，采用能自然说出口的中文；战斗紧张感不等于一律短句或一律粗口。",
                None,
            )
        return (
            "角色对白",
            "根据说话者身份、关系、教育程度、情绪和前后文决定口语或书面程度；不要统一成现代口语，也不要无依据古雅化。",
            None,
        )

    if "battle" in value or "_lose_" in value or "_win_" in value:
        return (
            "战斗旁白或战斗反馈",
            "动作要清楚、紧凑、顺口，保留机制事实但避免机制腔；普通动作优先现代自然叙述，不为增强力度滥用偏书面词。",
            None,
        )

    if stem.startswith("main_scene"):
        return (
            "成人剧情旁白",
            "保持原文身体、动作、视角和强度，叙述应连贯自然；不弱化，也不额外情色化或堆砌露骨词。",
            None,
        )

    return (
        "剧情旁白或场景叙述",
        "采用连贯、沉浸且符合当前场景张力的现代中文叙述；可自然重排，但不要统一成口语、说明书腔或伪古文。",
        None,
    )


def audit_context(records: list[Record], project_root: Path) -> tuple[list[dict], dict]:
    """Classify the minimum context each record needs before translation."""

    duplicate_counts = Counter(record.source for record in records if record.source)
    aliases = character_aliases(project_root)
    alias_names = set(aliases.values()) - GENERIC_CHARACTER_NAMES
    old_term_candidates: dict[str, set[str]] = defaultdict(set)
    for record in records:
        if record.kind == "menu" and record.old_reference is not None:
            old_term_candidates[record.source].add(record.old_reference)
    old_package = project_root / "game" / "tl" / "schinese"
    if old_package.exists():
        _, old_menus = package_values(old_package, "schinese")
        for (_, source, _), translated in old_menus.items():
            old_term_candidates[source].add(translated)
    old_terms = {
        source: sorted(references)
        for source, references in old_term_candidates.items()
        if source and len(references) == 1
    }
    audited: list[dict] = []
    reason_counts: Counter[str] = Counter()
    field_counts: Counter[str] = Counter()
    file_stats: dict[str, dict] = defaultdict(
        lambda: {
            "records": 0,
            "dialogue": 0,
            "menu": 0,
            "speakers": set(),
            "scene_families": set(),
            "risk_records": 0,
        }
    )

    for record in records:
        words = set(re.findall(r"[a-z]+", record.source.lower()))
        reasons: list[str] = []
        role, register_note, world_context = translation_context(record)
        fields: set[str] = {"translation-policy", "text-role", "register-note"}
        if world_context:
            fields.add("world-context")

        if record.source == "":
            reasons.append("empty-source")
        if record.kind == "menu":
            reasons.append("menu-string")
            fields.update({"ui-role", "menu-neighbors"})
        else:
            fields.add("scene-profile")
        if record.speaker:
            reasons.append("speaker-attributed")
            fields.add("speaker-profile")
            if record.speaker not in aliases:
                reasons.append("unresolved-speaker-alias")
        if has_protected_content(record):
            reasons.append("protected-syntax")
            fields.add("placeholder-contract")
        if len(record.current_parts) > 1:
            reasons.append("existing-split-output")
            fields.add("split-output-contract")
        if len(record.source) <= 45:
            reasons.append("short-or-fragment")
            fields.add("neighbor-context")
        if words & PRONOUN_WORDS:
            reasons.append("pronoun-reference")
            fields.add("neighbor-context")
        if words & DEICTIC_WORDS:
            reasons.append("deictic-reference")
            fields.add("neighbor-context")
        if "..." in record.source or "…" in record.source:
            reasons.append("ellipsis-or-turn-boundary")
            fields.add("neighbor-context")
        if words & QUANTITY_WORDS or re.search(r"\d", record.source):
            reasons.append("quantity-or-number")
            fields.add("quantity-context")
        if words & CONDITION_WORDS:
            reasons.append("condition-or-causality")
            fields.add("scene-profile")
        if "?" in record.source or "!" in record.source:
            reasons.append("dialogue-act")
            fields.add("neighbor-context")
        if duplicate_counts[record.source] > 1:
            reasons.append("repeated-source")
            fields.add("same-source-disambiguation")
        if is_sensitive(record):
            reasons.append("sensitive-content")
            fields.add("content-tone")
        if record.old_reference is not None:
            fields.add("old-reference")
        terms = matched_terms(record.source, alias_names)
        term_references = {
            term: old_terms[term]
            for term in terms
            if term in old_terms and old_terms[term][0] != term
        }
        if terms:
            reasons.append("known-entity-term")
            fields.add("term-glossary")

        # Empty source nodes are structural placeholders, not API translation
        # work.  Everything else gets a compact context tier for scheduling.
        if record.source == "":
            tier = "skip"
            fields = {"structural-placeholder"}
        elif len(reasons) >= 3 or "protected-syntax" in reasons or "repeated-source" in reasons:
            tier = "focused"
        elif reasons or record.old_reference is not None:
            tier = "standard"
        else:
            tier = "minimal"

        for reason in reasons:
            reason_counts[reason] += 1
        for field in fields:
            field_counts[field] += 1

        stats = file_stats[record.file]
        stats["records"] += 1
        stats[record.kind] += 1
        stats["speakers"].add(record.speaker) if record.speaker else None
        stats["scene_families"].add(scene_family(record))
        stats["risk_records"] += tier in {"focused", "standard"}

        audited.append(
            {
                "ordinal": record.ordinal,
                "file": record.file,
                "id": record.id,
                "kind": record.kind,
                "scene_family": scene_family(record),
                "tier": tier,
                "reasons": reasons,
                "context_fields": sorted(fields),
                "speaker": record.speaker or None,
                "speaker_name": aliases.get(record.speaker) if record.speaker else None,
                "matched_terms": terms,
                "term_references": term_references,
                "same_source_count": duplicate_counts[record.source] if record.source else 0,
                "has_old_reference": record.old_reference is not None,
                "text_role": role,
                "register_note": register_note,
                "world_context": world_context,
            }
        )

    serializable_files = {}
    for file_name, stats in sorted(file_stats.items()):
        serializable_files[file_name] = {
            **stats,
            "speakers": sorted(stats["speakers"]),
            "scene_families": sorted(stats["scene_families"]),
        }

    metadata = {
        "records": len(records),
        "tiers": dict(Counter(item["tier"] for item in audited)),
        "reason_counts": dict(sorted(reason_counts.items())),
        "context_field_counts": dict(sorted(field_counts.items())),
        "duplicate_source_values": sum(count > 1 for count in duplicate_counts.values()),
        "character_aliases": dict(sorted(aliases.items())),
        "canonical_term_references": dict(sorted(old_terms.items())),
        "files": serializable_files,
        "injection_policy": {
            "minimal": ["translation-policy"],
            "standard": ["translation-policy", "scene-profile-or-ui-role", "relevant-old-reference", "relevant-glossary"],
            "focused": ["translation-policy", "scene-profile-or-ui-role", "speaker-profile", "neighbor-context", "placeholder-contract", "relevant-old-reference", "relevant-glossary"],
            "skip": ["preserve-structural-placeholder"],
        },
    }
    return audited, metadata


def write_dict_jsonl(path: Path, records: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def estimate_record_prompt_chars(record: dict) -> int:
    """Estimate compact request size without requiring a context audit."""

    fields = (
        record.get("file"),
        record.get("id"),
        record.get("kind"),
        record.get("speaker"),
        record.get("source"),
        record.get("old_reference"),
        record.get("context_before"),
        record.get("context_after"),
    )
    return 128 + sum(len(str(value)) for value in fields if value)


def split_records(records: list[dict], max_records: int, max_chars: int) -> list[list[dict]]:
    """Split records in stable order using both count and prompt-size limits."""

    if max_records <= 0 or max_chars <= 0:
        raise ValueError("批次上限必须为正数")
    batches: list[list[dict]] = []
    current: list[dict] = []
    current_chars = 0
    for record in sorted(records, key=lambda value: int(value["ordinal"])):
        estimate = estimate_record_prompt_chars(record)
        if current and (len(current) >= max_records or current_chars + estimate > max_chars):
            batches.append(current)
            current = []
            current_chars = 0
        current.append(record)
        current_chars += estimate
    if current:
        batches.append(current)
    return batches


def split_command(args: argparse.Namespace) -> int:
    records = [asdict(record) for record in read_jsonl(args.records)]
    if not records:
        raise ValueError("输入记录为空")
    batches = split_records(records, args.max_records, args.max_chars)
    args.output.mkdir(parents=True, exist_ok=True)
    manifest_batches = []
    for index, batch in enumerate(batches, 1):
        path = args.output / f"{args.prefix}-{index:04d}.jsonl"
        write_dict_jsonl(path, batch)
        manifest_batches.append(
            {
                "file": path.name,
                "records": len(batch),
                "first_ordinal": batch[0]["ordinal"],
                "last_ordinal": batch[-1]["ordinal"],
                "estimated_chars": sum(estimate_record_prompt_chars(record) for record in batch),
            }
        )
    manifest = {
        "records": len(records),
        "batches": len(batches),
        "max_records": args.max_records,
        "max_chars": args.max_chars,
        "items": manifest_batches,
    }
    (args.output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"records": len(records), "batches": len(batches), "output": str(args.output)}, ensure_ascii=False))
    return 0


def context_audit_command(args: argparse.Namespace) -> int:
    args.output.mkdir(parents=True, exist_ok=True)
    records = read_jsonl(args.catalog)
    audited, metadata = audit_context(records, args.project_root)
    write_dict_jsonl(args.output / "context-audit.jsonl", audited)
    (args.output / "context-audit.meta.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"records": len(audited), "tiers": metadata["tiers"], "output": str(args.output)}, ensure_ascii=False))
    return 0


def extract_command(args: argparse.Namespace) -> int:
    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    records = extract_records(args.package, args.language, args.old_package)
    if not records:
        raise ValueError("没有提取到可翻译条目")
    catalog_path = output / "catalog.jsonl"
    write_jsonl(catalog_path, records)
    metadata = {
        "language": args.language,
        "package": str(args.package),
        "old_package": str(args.old_package) if args.old_package else None,
        "records": len(records),
        "dialogue": sum(record.kind == "dialogue" for record in records),
        "menu": sum(record.kind == "menu" for record in records),
        "empty_source": sum(record.source == "" for record in records),
        "old_references": sum(record.old_reference is not None for record in records),
        "files": sorted({record.file for record in records}),
    }
    (output / "catalog.meta.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(metadata, ensure_ascii=False))
    return 0


def pilot_command(args: argparse.Namespace) -> int:
    args.output.mkdir(parents=True, exist_ok=True)
    records = read_jsonl(args.catalog)
    pilot = choose_pilot(records, args.count)
    if len(pilot) < args.count:
        raise ValueError(f"只能生成 {len(pilot)} 条校准样本，目标为 {args.count} 条")
    write_jsonl(args.output / "pilot.jsonl", pilot)
    write_prompt(args.output / "pilot.input.tsv", pilot)
    manifest = {
        "count": len(pilot),
        "ordinals": [record.ordinal for record in pilot],
        "format": "ordinal kind speaker source old_reference context_before context_after",
        "output_contract": "按输入顺序输出同样数量的纯译文行；不输出编号、引号、代码或解释；\\n 保持转义。",
    }
    (args.output / "pilot.manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"count": len(pilot), "output": str(args.output)}, ensure_ascii=False))
    return 0


def stats_command(args: argparse.Namespace) -> int:
    records = read_jsonl(args.catalog)
    by_file = Counter(record.file for record in records)
    summary = {
        "records": len(records),
        "dialogue": sum(record.kind == "dialogue" for record in records),
        "menu": sum(record.kind == "menu" for record in records),
        "files": len(by_file),
        "empty_source": sum(record.source == "" for record in records),
        "old_references": sum(record.old_reference is not None for record in records),
        "context_records": sum(record.context_before is not None or record.context_after is not None for record in records),
        "largest_files": by_file.most_common(8),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract = subparsers.add_parser("extract", help="提取稳定 ID、英文源和可选旧版参考")
    extract.add_argument("--package", type=Path, required=True)
    extract.add_argument("--old-package", type=Path)
    extract.add_argument("--language", default="schinese_rewrite")
    extract.add_argument("--output", type=Path, required=True)
    extract.set_defaults(function=extract_command)

    pilot = subparsers.add_parser("pilot", help="从 catalog 生成多样化校准样本")
    pilot.add_argument("--catalog", type=Path, required=True)
    pilot.add_argument("--output", type=Path, required=True)
    pilot.add_argument("--count", type=int, default=200)
    pilot.set_defaults(function=pilot_command)

    stats = subparsers.add_parser("stats", help="显示 catalog 的紧凑统计")
    stats.add_argument("--catalog", type=Path, required=True)
    stats.set_defaults(function=stats_command)

    context = subparsers.add_parser("audit-context", help="审计每条记录需要注入的上下文")
    context.add_argument("--catalog", type=Path, required=True)
    context.add_argument("--project-root", type=Path, default=Path("."))
    context.add_argument("--output", type=Path, required=True)
    context.set_defaults(function=context_audit_command)

    split = subparsers.add_parser("split", help="按记录数和估算输入大小切分 JSONL 批次")
    split.add_argument("--records", type=Path, required=True)
    split.add_argument("--output", type=Path, required=True)
    split.add_argument("--max-records", type=int, default=25)
    split.add_argument("--max-chars", type=int, default=24000)
    split.add_argument("--prefix", default="batch")
    split.set_defaults(function=split_command)
    return parser


if __name__ == "__main__":
    arguments = build_parser().parse_args()
    raise SystemExit(arguments.function(arguments))
