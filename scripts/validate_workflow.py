#!/usr/bin/env python3
"""Validate GitHub Actions and repository path contracts."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Iterable

import yaml


WORKFLOW_PATH = Path(".github/workflows/scrape-and-generate-rss.yml")
REQUIRED_JOBS = {"scrape-and-generate-rss", "deploy-on-push", "deploy-after-scrape"}
REQUIRED_RUN_COMMANDS = {
    "python -m scripts.enhanced_scraper",
    "python -m pipeline.run_all",
    "python -m scripts.monitor",
}
REQUIRED_PATHS = {
    "requirements.txt",
    "scripts/enhanced_scraper.py",
    "scripts/monitor.py",
    "scripts/config.py",
    "scripts/feed_generator.py",
    "pipeline/run_all.py",
    "pipeline/article_content.py",
    "api/rss_status.json",
    "api/feed.json",
    "feeds/top.xml",
    "Docs/reference/ai-relevance-rubric.md",
    "Docs/reference/business-and-technical-importance-rubric.md",
}
REQUIRED_STAGE_PATTERNS = {
    "*rss_feed*.xml",
    "*rss_feed*.atom",
    "*rss_feed*.json",
    "aggregated*.xml",
    "aggregated*.atom",
    "aggregated*.json",
    "api/*.json",
    "feeds/*",
    "data/*.json",
    "derived/*.json",
    "derived/*.jsonl",
    "reports/*.json",
    "reports/*.md",
    "reports/aggregation/*.json",
    "reports/aggregation/*.md",
}
SITE_STATUS_CONSUMERS = {"about.md", "feeds.html", "status.html"}


def _flatten_run_commands(workflow: dict) -> list[str]:
    runs: list[str] = []
    for job in workflow.get("jobs", {}).values():
        if not isinstance(job, dict):
            continue
        for step in job.get("steps", []):
            if isinstance(step, dict) and isinstance(step.get("run"), str):
                runs.append(step["run"])
    return runs


def _check(condition: bool, message: str, errors: list[str], verbose: bool) -> None:
    if condition:
        if verbose:
            print(f"ok   {message}")
    else:
        if verbose:
            print(f"fail {message}")
        errors.append(message)


def _contains_all(haystacks: Iterable[str], needles: Iterable[str]) -> set[str]:
    combined = "\n".join(haystacks)
    return {needle for needle in needles if needle in combined}


def validate(verbose: bool = True) -> list[str]:
    errors: list[str] = []

    _check(WORKFLOW_PATH.is_file(), f"workflow exists: {WORKFLOW_PATH}", errors, verbose)
    if not WORKFLOW_PATH.is_file():
        return errors

    with WORKFLOW_PATH.open("r", encoding="utf-8") as handle:
        workflow = yaml.safe_load(handle) or {}

    jobs = workflow.get("jobs", {}) if isinstance(workflow, dict) else {}
    job_names = set(jobs.keys()) if isinstance(jobs, dict) else set()
    _check(REQUIRED_JOBS.issubset(job_names), f"required jobs present: {sorted(REQUIRED_JOBS)}", errors, verbose)

    run_commands = _flatten_run_commands(workflow)
    found_commands = _contains_all(run_commands, REQUIRED_RUN_COMMANDS)
    _check(found_commands == REQUIRED_RUN_COMMANDS, f"required run commands present: {sorted(REQUIRED_RUN_COMMANDS)}", errors, verbose)

    workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")
    found_stage_patterns = {pattern for pattern in REQUIRED_STAGE_PATTERNS if pattern in workflow_text}
    _check(found_stage_patterns == REQUIRED_STAGE_PATTERNS, "generated artifact staging patterns present", errors, verbose)

    for path_text in sorted(REQUIRED_PATHS):
        _check(Path(path_text).exists(), f"required path exists: {path_text}", errors, verbose)

    for consumer in sorted(SITE_STATUS_CONSUMERS):
        path = Path(consumer)
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        _check("/api/rss_status.json" in text, f"{consumer} consumes /api/rss_status.json", errors, verbose)

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("\nWorkflow validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nWorkflow validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())