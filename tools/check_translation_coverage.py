"""Check a generated Ren'Py translation package against a developer catalog.

The catalog is produced from the developer ``.rpyc`` files by the existing
staging extractor.  This checker is intentionally independent of the model
and of the old translation package: it verifies identifiers, menu keys,
non-empty values, ``pass`` blocks, and exact preservation of Ren'Py markup.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import Counter
from pathlib import Path


MARKUP = re.compile(r"(\[[^\]\r\n]*\]|\{[^}\r\n]*\}|\\n|\r?\n)")
BLOCK = re.compile(
    r"(?ms)^translate (?P<language>\w+) (?P<header>[^\r\n]+):\r?\n"
    r"(?P<body>.*?)(?=^translate \w+ |\Z)"
)
STRING_LINE = re.compile(r'^\s*(?:(?:[A-Za-z_]\w*)\s+)?(?P<value>"(?:\\.|[^"\\])*")')
OLD_LINE = re.compile(r'^\s*old\s+(?P<value>"(?:\\.|[^"\\])*")\s*$')
NEW_LINE = re.compile(r'^\s*new\s+(?P<value>"(?:\\.|[^"\\])*")\s*$')
DYNAMIC = re.compile(
    r'(?<![A-Za-z0-9_])(?:__|_p?)\(\s*(?P<value>"""(?:.|\n)*?"""|'
    r"'''(?:.|\n)*?'''|\"(?:\\.|[^\"\\])*\"|"
    r"'(?:\\.|[^'\\])*')",
    re.S,
)


def quoted(pattern: re.Pattern[str], line: str) -> str | None:
    match = pattern.match(line)
    if not match:
        return None
    return ast.literal_eval(match.group("value"))


def dynamic_strings(source_root: Path) -> set[str]:
    values: set[str] = set()
    for path in sorted(source_root.glob("*.rpy")):
        text = path.read_text(encoding="utf-8-sig")
        for match in DYNAMIC.finditer(text):
            try:
                value = ast.literal_eval(match.group("value"))
            except (SyntaxError, ValueError):
                continue
            if isinstance(value, str) and value:
                values.add(value)
    return values


def package_entries(package: Path, language: str):
    dialogue: dict[str, str] = {}
    passes: set[str] = set()
    strings: dict[str, str] = {}
    duplicate_dialogue: Counter[str] = Counter()
    duplicate_strings: Counter[str] = Counter()

    for path in sorted(package.rglob("*.rpy")):
        text = path.read_text(encoding="utf-8-sig")
        for block in BLOCK.finditer(text):
            if block.group("language") != language:
                continue
            header = block.group("header")
            body = block.group("body")
            if header == "strings":
                old = new = None
                for line in body.splitlines():
                    old = quoted(OLD_LINE, line) or old
                    new = quoted(NEW_LINE, line) or new
                    if old is not None and new is not None:
                        duplicate_strings[old] += 1
                        strings[old] = new
                        old = new = None
                continue

            values = [
                value
                for line in body.splitlines()
                if (value := quoted(STRING_LINE, line)) is not None
            ]
            if "pass" in {line.strip() for line in body.splitlines()}:
                passes.add(header)
            if values:
                duplicate_dialogue[header] += 1
                dialogue[header] = "".join(values)
    return dialogue, strings, passes, duplicate_dialogue, duplicate_strings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--language", default="schinese_rewrite")
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    source_dialogue = {
        entry["identifier"]: entry["nodes"][0]["what"]
        for entry in catalog["dialogue"]
    }
    source_root = args.source_root or args.package.parents[1]
    source_strings = {entry["old"] for entry in catalog["menu_strings"]}
    source_strings.update(dynamic_strings(source_root))
    dialogue, strings, passes, duplicate_dialogue, duplicate_strings = package_entries(
        args.package, args.language
    )

    missing_dialogue = sorted(set(source_dialogue) - set(dialogue))
    missing_strings = sorted(source_strings - set(strings))
    empty_source_dialogue = sorted(
        key for key, value in source_dialogue.items() if not value.strip()
    )
    empty_dialogue = sorted(
        key
        for key, value in dialogue.items()
        if not value.strip() and source_dialogue.get(key, "").strip()
    )
    empty_strings = sorted(key for key, value in strings.items() if not value.strip())
    placeholder_mismatch = {
        key: {"source": MARKUP.findall(source), "translated": MARKUP.findall(dialogue[key])}
        for key, source in source_dialogue.items()
        if key in dialogue and MARKUP.findall(source) != MARKUP.findall(dialogue[key])
    }
    string_placeholder_mismatch = {
        key: {"source": MARKUP.findall(key), "translated": MARKUP.findall(strings[key])}
        for key in source_strings
        if key in strings and MARKUP.findall(key) != MARKUP.findall(strings[key])
    }
    report = {
        "source_dialogue": len(source_dialogue),
        "translated_dialogue": len(dialogue),
        "source_menu_strings": len(source_strings),
        "translated_menu_strings": len(strings),
        "missing_dialogue": missing_dialogue,
        "missing_menu_strings": missing_strings,
        "empty_dialogue": empty_dialogue,
        "empty_source_dialogue": empty_source_dialogue,
        "empty_menu_strings": empty_strings,
        "pass_blocks": sorted(passes),
        "placeholder_mismatch": placeholder_mismatch,
        "menu_placeholder_mismatch": string_placeholder_mismatch,
        "duplicate_dialogue_ids": sorted(k for k, v in duplicate_dialogue.items() if v > 1),
        "duplicate_menu_strings": sorted(k for k, v in duplicate_strings.items() if v > 1),
    }
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    scalar = {
        key: value
        for key, value in report.items()
        if isinstance(value, int)
    }
    print(json.dumps(scalar, ensure_ascii=False))
    failures = {
        key: value
        for key, value in report.items()
        if key != "empty_source_dialogue"
        if isinstance(value, list) and value
        or isinstance(value, dict) and value
    }
    if failures:
        for key, value in failures.items():
            print(f"{key}: {len(value)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
