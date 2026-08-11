"""Dispatch independent sub2api translation batches with a hard concurrency cap."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


MAX_CONCURRENCY = 6


def result_attempts(output_root: Path, batch_path: Path) -> list[Path]:
    """Return this batch's attempts in newest-first order."""

    batch_root = output_root / batch_path.stem
    return sorted(batch_root.glob("attempt-*"), reverse=True)


def successful_attempt(output_root: Path, batch_path: Path) -> Path | None:
    """Find an already validated result that can be reused after a restart."""

    expected_records = sum(
        1
        for line in batch_path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    )
    for attempt in result_attempts(output_root, batch_path):
        metadata_path = attempt / "result.meta.json"
        translations_path = attempt / "translations.tsv"
        if not metadata_path.is_file() or not translations_path.is_file():
            continue
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if metadata.get("status") != "completed" or metadata.get("output_lines") != expected_records:
            continue
        actual_records = sum(
            1
            for line in translations_path.read_text(encoding="utf-8-sig").splitlines()
            if line.strip()
        )
        if actual_records == expected_records:
            return attempt
    return None


def next_attempt_number(output_root: Path, batch_path: Path) -> int:
    """Choose a fresh attempt directory without overwriting interrupted work."""

    numbers = []
    for attempt in result_attempts(output_root, batch_path):
        match = attempt.name.removeprefix("attempt-")
        if match.isdigit():
            numbers.append(int(match))
    return max(numbers, default=0) + 1


def run_batch(args: argparse.Namespace, batch_path: Path, api_key: str, attempt: int) -> dict:
    output = args.output / batch_path.stem / f"attempt-{attempt:02d}"
    output.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        str(Path(__file__).with_name("sub2api_translate.py")),
        "--records",
        str(batch_path),
        "--context-audit",
        str(args.context_audit),
        "--output",
        str(output),
        "--endpoint",
        args.endpoint,
        "--model",
        args.model,
        "--max-output-tokens",
        str(args.max_output_tokens),
        "--reasoning-effort",
        args.reasoning_effort,
    ]
    environment = os.environ.copy()
    environment["OUTLAND_SUB2API_API_KEY"] = api_key
    completed = subprocess.run(
        command,
        cwd=Path.cwd(),
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    (output / "dispatcher.stdout.txt").write_text(completed.stdout, encoding="utf-8", newline="\n")
    (output / "dispatcher.stderr.txt").write_text(completed.stderr, encoding="utf-8", newline="\n")
    return {
        "batch": batch_path.name,
        "output": str(output),
        "attempt": attempt,
        "returncode": completed.returncode,
        "status": "completed" if completed.returncode == 0 else "failed",
    }


def dispatch_command(args: argparse.Namespace) -> int:
    if not 1 <= args.max_concurrency <= MAX_CONCURRENCY:
        raise ValueError(f"并发数必须在 1 到 {MAX_CONCURRENCY} 之间")
    if args.retries < 0:
        raise ValueError("重试次数不能为负数")
    api_key = args.api_key or os.environ.get("OUTLAND_SUB2API_API_KEY")
    if not api_key:
        raise ValueError("请通过 --api-key 或 OUTLAND_SUB2API_API_KEY 提供本地 API key")
    batches = sorted(args.batches.glob("*.jsonl"))
    if not batches:
        raise ValueError(f"批次目录为空：{args.batches}")
    args.output.mkdir(parents=True, exist_ok=True)
    batches_by_name = {path.name: path for path in batches}

    results: list[dict] = []
    pending = []
    for batch in batches:
        reused = successful_attempt(args.output, batch)
        if reused is None:
            pending.append(batch)
        else:
            results.append(
                {
                    "batch": batch.name,
                    "output": str(reused),
                    "attempt": int(reused.name.removeprefix("attempt-")),
                    "returncode": 0,
                    "status": "reused",
                }
            )
    for attempt in range(1, args.retries + 2):
        if not pending:
            break
        current_results: list[dict] = []
        with ThreadPoolExecutor(max_workers=args.max_concurrency) as executor:
            futures = {
                executor.submit(
                    run_batch,
                    args,
                    path,
                    api_key,
                    next_attempt_number(args.output, path),
                ): path
                for path in pending
            }
            for future in as_completed(futures):
                current_results.append(future.result())
        results.extend(current_results)
        pending = [
            batches_by_name[result["batch"]]
            for result in current_results
            if result["status"] == "failed"
        ]
    results.sort(key=lambda result: (result["batch"], result["attempt"]))
    metadata = {
        "batches": len(batches),
        "max_concurrency": args.max_concurrency,
        "retries": args.retries,
        "endpoint": args.endpoint,
        "model": args.model,
        "completed": len(batches) - len(pending),
        "failed": len(pending),
        "reused": sum(result["status"] == "reused" for result in results),
        "submitted": sum(result["status"] in {"completed", "failed"} for result in results),
        "results": results,
    }
    (args.output / "dispatch.meta.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {key: metadata[key] for key in ("batches", "max_concurrency", "retries", "completed", "failed")},
            ensure_ascii=False,
        )
    )
    return 0 if metadata["failed"] == 0 else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batches", type=Path, required=True, help="每个 JSONL 文件代表一个独立翻译批次")
    parser.add_argument("--context-audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8080/v1/responses")
    parser.add_argument("--model", default="gpt-5.6-luna")
    parser.add_argument("--api-key")
    parser.add_argument("--max-output-tokens", type=int, default=16000)
    parser.add_argument("--reasoning-effort", choices=("default", "low", "medium", "high"), default="medium")
    parser.add_argument("--max-concurrency", type=int, default=MAX_CONCURRENCY)
    parser.add_argument("--retries", type=int, default=2)
    parser.set_defaults(function=dispatch_command)
    return parser


if __name__ == "__main__":
    try:
        arguments = build_parser().parse_args()
        raise SystemExit(arguments.function(arguments))
    except (RuntimeError, ValueError) as error:
        print(f"错误：{error}", file=sys.stderr)
        raise SystemExit(1)
