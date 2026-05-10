# GitHub Actions Extension Guide

## Bottom Line

Extend the pipeline by preserving three contracts:

1. Public feed URLs stay stable.
2. Generated artifacts are staged and committed deliberately.
3. Site-facing JSON endpoints stay aligned with the pages that fetch them.

If a change violates one of those contracts, treat it as an architecture change, not a small workflow edit.

## Decision Framework

Before editing the workflow, answer these questions:

| Question | Why It Matters |
| --- | --- |
| Is this a public output or an internal artifact? | Public outputs need stable URLs and compatibility review. |
| Does this produce a new file? | The workflow staging allowlist must include it. |
| Does this need a new secret? | Scheduled runs fail differently than local runs when secrets are absent. |
| Does this change source configuration? | `_config.yml` and `sources.yml` feed different parts of the system. |
| Does this change deploy timing? | Pages deployment is tied to generated artifact refresh. |

## Common Extension Patterns

### Add Or Modify A Top Stories Source

Use this when the source belongs in the ranked Top Stories pipeline.

1. Update `sources.yml`.
2. Confirm source fields match the expected source model.
3. Run `python -m pipeline.run_all` locally if you want a full data refresh.
4. Run `python -m scripts.monitor` to update status after output changes.
5. Confirm `api/feed.json`, `feeds/top.*`, `data/*.json`, `derived/*.json*`, and `reports/pipeline_report.*` are expected.

Use this path for source ranking, clustering, deduplication, LLM summaries, and Top Stories output.

### Add Or Modify An Aggregated Feed

Use this when the output should be a public RSS-style feed in the root namespace.

1. Update `_config.yml` under `feeds` with `aggregated: true`.
2. Choose the public output path carefully, usually root-level `aggregated_*.xml`.
3. Make sure alternate formats are expected: RSS 1.0, Atom, JSON.
4. Run `python -m scripts.enhanced_scraper` if you need to generate it locally.
5. Run `python -m scripts.monitor` so `api/rss_status.json` includes the new feed.
6. Verify the workflow staging allowlist covers the new generated filenames.

Use this path for subscriber-facing feeds that should remain stable over time.

### Add A New Pipeline Stage

Use this when you need a new transformation between ingestion and publishing.

1. Add a module under `pipeline/`.
2. Wire it into `pipeline/run_all.py`.
3. Define any new artifact paths in `pipeline/constants.py`.
4. Write outputs through `pipeline/io_utils.py` helpers where practical.
5. Add generated artifacts to the workflow staging allowlist.
6. Update [Docs/architecture/data-contracts.md](../architecture/data-contracts.md) if the JSON contract changes.
7. Update [Docs/architecture/github-actions-pipeline-architecture.md](../architecture/github-actions-pipeline-architecture.md) if the component boundary changes.

### Add A New Site-Facing API File

Use this when the website needs new browser-readable JSON.

1. Prefer `api/<name>.json` for public site APIs.
2. Add the producer in `scripts/` or `pipeline/`, depending on ownership.
3. Update the consuming page to fetch the new path.
4. Ensure `_config.yml` does not exclude the API file path from the site build.
5. Confirm `.github/workflows/scrape-and-generate-rss.yml` stages `api/*.json` or the specific path.

### Add A New Internal State File

Use this for caches, checkpoints, logs, or run state.

1. Prefer `derived/` for machine state.
2. Prefer `reports/` for human-readable or diagnostic output.
3. Avoid repo root unless the file is a public URL contract.
4. Add the file path to the workflow staging allowlist.
5. Add monitor coverage if the site or operators depend on it.

### Add A New Deployment Target

Use this only when the site needs another environment or publishing path.

1. Add a separate deploy job rather than overloading the existing Pages jobs.
2. Keep permissions minimal.
3. Add or adjust concurrency so deploy jobs do not race.
4. Document rollback behavior in [github-actions-runbook.md](github-actions-runbook.md).
5. Validate the build command locally before relying on Actions.

## Contracts To Preserve

| Contract | Current Location | Extension Rule |
| --- | --- | --- |
| Public root feeds | `ai_rss_feed.*`, `aggregated_*.*`, archives | Do not move without redirect and subscriber review. |
| Top Stories feeds | `feeds/top.*` | Keep path stable unless creating a versioned replacement. |
| Site status JSON | `api/rss_status.json` | Update both producer and consumers if changed. |
| Internal state | `derived/` | Keep machine state out of root. |
| Operational reports | `reports/` | Keep reports out of root and stage them deliberately. |
| Python entrypoints | `scripts/` modules | Run with `python -m scripts.<module>`. |
| Importance rubric | `Docs/reference/business-and-technical-importance-rubric.md` | Update code constants if moved. |

## Minimum Validation Checklist

Run this checklist before pushing workflow or pipeline changes:

```bash
source .venv/bin/activate
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/config.py scripts/feed_generator.py scripts/enhanced_scraper.py scripts/scrape_to_rss.py scripts/monitor.py scripts/validate_setup.py pipeline/publish.py
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_workflow
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_setup
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.monitor
bundle exec jekyll build --destination /tmp/rss-tedt-extension-build
find . -maxdepth 3 \( -name '__pycache__' -o -name '.DS_Store' \) -not -path './.venv/*' -not -path './vendor/*' -print | sort
```

If the change touches workflow syntax and `actionlint` is installed:

```bash
actionlint .github/workflows/scrape-and-generate-rss.yml
```

## Review Checklist

- Public URL paths are unchanged or intentionally versioned.
- Workflow staging globs include every generated artifact that must persist.
- New secrets are documented with degraded behavior.
- `api/rss_status.json` still reflects the data the site depends on.
- Jekyll build succeeds.
- Local generated bytecode or macOS metadata was removed before finalizing.
- Documentation was updated in `Docs/`, not scattered in the repo root.
