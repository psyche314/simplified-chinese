"""从 Ren'Py 语言包中随机抽取译文。

用法::

    python tools/sample_translations.py schinese_rewrite 20
    python tools/sample_translations.py french 10 --seed 42

默认将 JSONL 写到标准输出；使用 ``--output`` 可以写入文件。每条记录
包含语言包文件、稳定翻译键、文本类型和当前译文。带有英文原文注释的
语言包还会附带 ``source``；其他旧语言包没有这类注释时该字段为 null。
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import random
import sys
from typing import TextIO


TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent
LANGUAGE_ROOT = REPO_ROOT / "game" / "tl"
LANGUAGES = ("french", "portuguese", "russian", "schinese", "schinese_rewrite")
SPLIT_MARKER = "␟"

# Keep the Ren'Py parser in one place.  These helpers understand generated
# strings blocks, escaped literals, and adjacent statements in a translation
# block; this script only adds random selection and output formatting.
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from translation_batches import (  # noqa: E402
    Block,
    dialogue_parts,
    parse_blocks,
    source_comment,
    stable_menu_id,
    string_pairs,
)


@dataclass(frozen=True)
class Translation:
    language: str
    file: str
    key: str
    id: str
    kind: str
    occurrence: int
    speaker: str | None
    source: str | None
    translation: str


def _positive_count(value: str) -> int:
    try:
        count = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("数量必须是大于 1 的整数") from error
    if count <= 1:
        raise argparse.ArgumentTypeError("数量必须是大于 1 的整数")
    return count


def _source_info(block: Block) -> tuple[str | None, str | None]:
    """Return optional speaker/source information from a generated block."""

    try:
        speaker, source, _ = source_comment(block)
    except ValueError:
        return None, None
    return speaker or None, source


def _dialogue_translation(block: Block) -> tuple[list[str], str | None, str | None] | None:
    """Parse a text-only block, skipping executable/empty translation blocks."""

    lines = block.lines
    if any(line.strip() == "pass" for line in lines[1:]):
        return None
    try:
        parts = dialogue_parts(block)
    except ValueError:
        # Ren'Py translation blocks may legally contain arbitrary code.  Such
        # blocks are not a single extractable translation and are left out.
        return None
    if not parts or not any(part.strip() for part in parts):
        return None
    speaker, source = _source_info(block)
    return parts, speaker, source


def collect_translations(language: str) -> list[Translation]:
    package = LANGUAGE_ROOT / language
    if not package.is_dir():
        raise ValueError(f"语言包不存在：{package}")

    records: list[Translation] = []
    menu_occurrences: dict[tuple[str, str], int] = {}
    dialogue_occurrences: dict[tuple[str, str], int] = {}

    for path in sorted(package.glob("*.rpy")):
        for block in parse_blocks(path, language):
            key = block.key
            if key.startswith("style ") or key in {"python", "early", "late"}:
                continue

            if key == "strings":
                for source, translation in string_pairs(block):
                    if not translation.strip():
                        continue
                    occurrence_key = (path.name, source)
                    occurrence = menu_occurrences.get(occurrence_key, 0)
                    menu_occurrences[occurrence_key] = occurrence + 1
                    records.append(
                        Translation(
                            language=language,
                            file=path.name,
                            key=key,
                            id=stable_menu_id(path.name, source, occurrence),
                            kind="menu",
                            occurrence=occurrence,
                            speaker=None,
                            source=source,
                            translation=translation,
                        )
                    )
                continue

            parsed = _dialogue_translation(block)
            if parsed is None:
                continue
            parts, speaker, source = parsed
            translation = SPLIT_MARKER.join(parts)
            occurrence_key = (path.name, key)
            occurrence = dialogue_occurrences.get(occurrence_key, 0)
            dialogue_occurrences[occurrence_key] = occurrence + 1
            record_id = f"{path.name}:{language}:{key}"
            if occurrence:
                record_id += f"#{occurrence + 1}"
            records.append(
                Translation(
                    language=language,
                    file=path.name,
                    key=key,
                    id=record_id,
                    kind="dialogue",
                    occurrence=occurrence,
                    speaker=speaker,
                    source=source,
                    translation=translation,
                )
            )

    if not records:
        raise ValueError(f"语言包中没有可抽取的非空译文：{package}")
    return records


def _write_jsonl(records: list[Translation], output: TextIO) -> None:
    for record in records:
        output.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("language_pos", nargs="?", choices=LANGUAGES, help="要抽取的语言包")
    parser.add_argument("count_pos", nargs="?", type=_positive_count, help="抽取数量，必须大于 1")
    parser.add_argument("--language", dest="language_opt", choices=LANGUAGES, help="要抽取的语言包")
    parser.add_argument("--count", dest="count_opt", type=_positive_count, help="抽取数量，必须大于 1")
    parser.add_argument("--seed", type=int, help="可选的随机种子，用于复现抽样结果")
    parser.add_argument("--output", type=Path, help="可选 JSONL 输出文件；默认写到标准输出")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    language = args.language_opt or args.language_pos
    count = args.count_opt or args.count_pos
    if language is None or count is None:
        raise ValueError("必须提供 language 和 count；可使用位置参数或 --language/--count")
    if args.language_opt and args.language_pos and args.language_opt != args.language_pos:
        raise ValueError("位置参数 language 与 --language 不一致")
    if args.count_opt and args.count_pos and args.count_opt != args.count_pos:
        raise ValueError("位置参数 count 与 --count 不一致")

    records = collect_translations(language)
    if count > len(records):
        raise ValueError(
            f"{language} 只有 {len(records)} 条可抽取译文，不能抽取 {count} 条"
        )

    rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()
    sampled = rng.sample(records, count)

    if args.output is None:
        _write_jsonl(sampled, sys.stdout)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8", newline="\n") as handle:
            _write_jsonl(sampled, handle)
        print(
            json.dumps(
                {"language": language, "available": len(records), "sampled": len(sampled), "output": str(args.output)},
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(f"错误：{error}", file=sys.stderr)
        raise SystemExit(2)
