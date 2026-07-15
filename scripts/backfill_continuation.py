from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def continuation_status(report: dict[str, Any], runs_remaining: int) -> dict[str, Any]:
    llm_status = report.get("llm_status")
    backlog = llm_status.get("backlog") if isinstance(llm_status, dict) else None
    if not isinstance(backlog, dict) or not backlog:
        return {
            "should_continue": False,
            "reason": "invalid_report",
            "backlog_before": 0,
            "backlog_remaining": 0,
            "next_runs_remaining": max(0, int(runs_remaining) - 1),
        }

    backlog_before = 0
    backlog_remaining = 0
    valid_stages = 0
    for counts in backlog.values():
        if not isinstance(counts, dict):
            continue
        try:
            before = max(0, int(counts.get("before") or 0))
            remaining = max(0, int(counts.get("remaining") or 0))
        except (TypeError, ValueError):
            continue
        backlog_before += before
        backlog_remaining += remaining
        valid_stages += 1

    next_runs_remaining = max(0, int(runs_remaining) - 1)
    if valid_stages == 0:
        reason = "invalid_report"
    elif backlog_remaining == 0:
        reason = "complete"
    elif backlog_remaining >= backlog_before:
        reason = "stalled"
    elif int(runs_remaining) <= 1:
        reason = "run_limit"
    else:
        reason = "progress"

    return {
        "should_continue": reason == "progress",
        "reason": reason,
        "backlog_before": backlog_before,
        "backlog_remaining": backlog_remaining,
        "next_runs_remaining": next_runs_remaining,
    }


def continuation_status_from_path(report_path: Path, runs_remaining: int) -> dict[str, Any]:
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        report = {}
    if not isinstance(report, dict):
        report = {}
    return continuation_status(report, runs_remaining)


def _write_github_output(path: Path, status: dict[str, Any]) -> None:
    lines = [
        f"should_continue={'true' if status['should_continue'] else 'false'}",
        f"reason={status['reason']}",
        f"backlog_before={status['backlog_before']}",
        f"backlog_remaining={status['backlog_remaining']}",
        f"next_runs_remaining={status['next_runs_remaining']}",
    ]
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate whether an enrichment backfill should continue.")
    parser.add_argument("report", type=Path)
    parser.add_argument("--runs-remaining", type=int, required=True)
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()

    status = continuation_status_from_path(args.report, args.runs_remaining)
    print(json.dumps(status, sort_keys=True))
    if args.github_output:
        _write_github_output(args.github_output, status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())