"""Apply validated sub2api translations back to the Ren'Py language package."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from sub2api_translate import EMPTY_SOURCE_MARKER, SPLIT_MARKER
from translation_batches import (
    STRING_ENTRY,
    TRANSLATE_HEADER,
    consume_string_statement,
    find_string_literal,
    read_jsonl,
    stable_menu_id,
)


def renpy_literal(value: str) -> str:
    """Encode a translation as one ordinary Ren'Py double-quoted literal.

    The API protocol represents embedded Ren'Py escapes such as backslash-n
    as two characters on one output line. Those recognized escape sequences
    must remain source escapes rather than being double-escaped by JSON
    encoding.
    """

    if value == EMPTY_SOURCE_MARKER:
        value = ""
    result = ['"']
    index = 0
    while index < len(value):
        character = value[index]
        if character == "\\":
            if index + 1 < len(value):
                result.append("\\" + value[index + 1])
                index += 2
            else:
                result.append("\\\\")
                index += 1
            continue
        if character == '"':
            result.append('\\"')
        elif character == "\n":
            result.append("\\n")
        elif character == "\r":
            result.append("\\r")
        elif character == "\t":
            result.append("\\t")
        elif ord(character) < 32:
            result.append(f"\\x{ord(character):02x}")
        else:
            result.append(character)
        index += 1
    result.append('"')
    return "".join(result)


def read_translations(result_root: Path) -> dict[int, str]:
    paths = [result_root] if result_root.is_file() else sorted(result_root.glob("**/translations.tsv"))
    if not paths:
        raise ValueError(f"结果目录没有 translations.tsv：{result_root}")
    translations: dict[int, str] = {}
    for path in paths:
        for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not line.strip():
                continue
            if "\t" not in line:
                raise ValueError(f"{path}:{line_number} 缺少 ordinal 分隔符")
            ordinal_text, translation = line.split("\t", 1)
            try:
                ordinal = int(ordinal_text)
            except ValueError as error:
                raise ValueError(f"{path}:{line_number} ordinal 无效：{ordinal_text!r}") from error
            if ordinal in translations:
                raise ValueError(f"ordinal 重复：{ordinal}（至少出现在 {path}）")
            translations[ordinal] = translation
    return translations


def statement_literal_parts(lines: list[str], start: int, end: int) -> tuple[str, str, str]:
    statement = "\n".join(lines[start:end])
    _, raw, literal_end = find_string_literal(statement)
    literal_start = statement.find(raw)
    if literal_start < 0:
        raise ValueError(f"字符串字面量定位失败：{statement!r}")
    return statement[:literal_start], statement[literal_end:], raw


def replace_statement(lines: list[str], start: int, end: int, value: str) -> list[str]:
    prefix, suffix, _ = statement_literal_parts(lines, start, end)
    rendered = prefix + renpy_literal(value) + suffix
    return rendered.splitlines()


def dialogue_spans(block_lines: list[str]) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    index = 1
    while index < len(block_lines):
        line = block_lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        _, next_index = consume_string_statement(block_lines, index)
        spans.append((index, next_index))
        index = next_index
    return spans


def render_dialogue(block_lines: list[str], translation: str) -> list[str]:
    spans = dialogue_spans(block_lines)
    if not spans:
        raise ValueError(f"翻译块没有载荷：{block_lines[0]!r}")
    parts = translation.split(SPLIT_MARKER)
    first_start, first_end = spans[0]
    last_start, last_end = spans[-1]
    prefix, _, _ = statement_literal_parts(block_lines, first_start, first_end)
    _, suffix, _ = statement_literal_parts(block_lines, last_start, last_end)
    rendered_payload: list[str] = []
    for index, part in enumerate(parts):
        rendered_suffix = suffix if index == len(parts) - 1 else ""
        rendered_payload.extend((prefix + renpy_literal(part) + rendered_suffix).splitlines())
    return block_lines[:first_start] + rendered_payload + block_lines[last_end:]


def menu_new_spans(file_name: str, block_lines: list[str]) -> list[tuple[str, int, int]]:
    spans: list[tuple[str, int, int]] = []
    old: str | None = None
    occurrence: Counter[tuple[str, str]] = Counter()
    index = 1
    while index < len(block_lines):
        line = block_lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        entry = STRING_ENTRY.match(line.strip())
        if entry is None:
            raise ValueError(f"未知 strings 条目：{file_name}: {line!r}")
        value, next_index = consume_string_statement(block_lines, index)
        if entry.group("kind") == "old":
            if old is not None:
                raise ValueError(f"连续 old 条目：{file_name}")
            old = value
        else:
            if old is None:
                raise ValueError(f"new 条目没有 old：{file_name}")
            key = (file_name, old)
            current_occurrence = occurrence[key]
            occurrence[key] += 1
            spans.append((stable_menu_id(file_name, old, current_occurrence), index, next_index))
            old = None
        index = next_index
    if old is not None:
        raise ValueError(f"old 条目没有 new：{file_name}")
    return spans


def render_file(path: Path, translations_by_id: dict[str, str]) -> tuple[str, int, set[str]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    starts = [index for index, line in enumerate(lines) if line.startswith("translate ")]
    output: list[str] = []
    cursor = 0
    changed_records = 0
    found_ids: set[str] = set()
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        block_lines = lines[start:end]
        match = TRANSLATE_HEADER.fullmatch(block_lines[0])
        if match is None or match.group("language") != "schinese_rewrite":
            output.extend(lines[cursor:start])
            output.extend(block_lines)
            cursor = end
            continue
        key = match.group("key")
        rendered = block_lines
        if key == "strings":
            replacements: list[tuple[int, int, list[str]]] = []
            for stable_id, block_start, block_end in menu_new_spans(path.name, block_lines):
                if stable_id in translations_by_id:
                    found_ids.add(stable_id)
                    replacements.append(
                        (
                            block_start,
                            block_end,
                            replace_statement(block_lines, block_start, block_end, translations_by_id[stable_id]),
                        )
                    )
            for block_start, block_end, replacement in reversed(replacements):
                rendered[block_start:block_end] = replacement
            changed_records += len(replacements)
        elif not key.startswith("style ") and key in translations_by_id:
            found_ids.add(key)
            rendered = render_dialogue(block_lines, translations_by_id[key])
            changed_records += 1
        output.extend(lines[cursor:start])
        output.extend(rendered)
        cursor = end
    output.extend(lines[cursor:])
    return "\n".join(output) + "\n", changed_records, found_ids


def load_catalog(path: Path) -> tuple[dict[int, object], dict[str, object]]:
    records = read_jsonl(path)
    by_ordinal = {record.ordinal: record for record in records}
    by_id = {record.id: record for record in records}
    if len(by_ordinal) != len(records) or len(by_id) != len(records):
        raise ValueError("catalog 含重复 ordinal 或稳定 ID")
    return by_ordinal, by_id


def apply_command(args: argparse.Namespace) -> int:
    by_ordinal, catalog_by_id = load_catalog(args.catalog)
    translations_by_ordinal = read_translations(args.results)
    missing = sorted(set(by_ordinal) - set(translations_by_ordinal))
    extra = sorted(set(translations_by_ordinal) - set(by_ordinal))
    if missing and not args.allow_partial:
        raise ValueError(f"结果缺少 ordinal：{missing}")
    if extra:
        raise ValueError(f"结果包含 catalog 外 ordinal：{extra}")
    translations_by_id = {
        catalog_by_id[by_ordinal[ordinal].id].id: translation
        for ordinal, translation in translations_by_ordinal.items()
        if ordinal in by_ordinal
    }

    target = args.target
    files_to_render = sorted(target.glob("*.rpy"))
    rendered_files: dict[Path, tuple[str, int, set[str]]] = {}
    changed_records = 0
    found_ids: set[str] = set()
    for path in files_to_render:
        rendered, changed, file_ids = render_file(path, translations_by_id)
        rendered_files[path] = (rendered, changed, file_ids)
        changed_records += changed
        found_ids.update(file_ids)

    selected_ids = {
        by_ordinal[ordinal].id
        for ordinal in translations_by_ordinal
        if ordinal in by_ordinal
    }
    if not args.allow_partial and found_ids != selected_ids:
        raise ValueError(f"目标语言包找不到稳定 ID：{sorted(selected_ids - found_ids)}")

    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
    if not args.dry_run:
        for path, (content, changed, _) in rendered_files.items():
            if not changed:
                continue
            destination = args.output / path.name if args.output else path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content, encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "catalog_records": len(by_ordinal),
                "translation_records": len(translations_by_ordinal),
                "changed_records": changed_records,
                "changed_files": sum(changed > 0 for _, changed, _ in rendered_files.values()),
                "dry_run": args.dry_run,
                "output": str(args.output) if args.output else str(target),
            },
            ensure_ascii=False,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--target", type=Path, default=Path("game/tl/schinese_rewrite"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--allow-partial", action="store_true")
    parser.set_defaults(function=apply_command)
    return parser


if __name__ == "__main__":
    arguments = build_parser().parse_args()
    try:
        raise SystemExit(arguments.function(arguments))
    except (OSError, ValueError) as error:
        print(f"错误：{error}")
        raise SystemExit(1)
