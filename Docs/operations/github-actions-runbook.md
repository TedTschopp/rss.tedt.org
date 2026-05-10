# GitHub Actions Runbook

## Normal Operation

The workflow runs every eight hours and can also be triggered manually. A successful scheduled/manual run should:

1. Generate public feed outputs.
2. Run the Top Stories pipeline.
3. Generate `api/rss_status.json`.
4. Commit generated artifacts if they changed.
5. Deploy the latest site to GitHub Pages.

Human pushes to `main` skip scraping and deploy the site only.

## Manual Run Procedure

1. Open the repository in GitHub.
2. Go to Actions.
3. Select `RSS Feed Hub - Scrape and Deploy`.
4. Choose `Run workflow` on `main`.
5. Watch the `scrape-and-generate-rss` job first, then `deploy-after-scrape`.

## Local Preflight

Before pushing pipeline changes, run:

```bash
source .venv/bin/activate
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_workflow
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_setup
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.monitor
bundle exec jekyll build --destination /tmp/rss-tedt-runbook-build
```

## Failure Triage

| Symptom | Likely Area | First Check |
| --- | --- | --- |
| Python install fails | Dependencies | `requirements.txt` and Python version. |
| Playwright browser fails | Scraper runtime | Playwright install step and Chromium dependency logs. |
| Public feeds not updated | Scraper or staging allowlist | `scripts.enhanced_scraper` logs and staged files list. |
| `feeds/top.*` not updated | Ranking pipeline | `pipeline.run_all` logs and `sources.yml`. |
| Site says status unavailable | Monitor or fetch path | `api/rss_status.json`, `feeds.html`, `about.md`. |
| Pages deploy fails | Jekyll or Pages | `bundle exec jekyll build` logs and `_config.yml`. |
| Workflow loops or duplicate deploys | Trigger logic | Actor conditions and deploy job `if` clauses. |

## Recovery Patterns

### Generated Artifact Is Bad

1. Stop and identify whether the artifact is public.
2. Fix the generator or source configuration.
3. Regenerate locally only if safe.
4. Run monitor and Jekyll validation.
5. Let GitHub Actions publish the corrected artifact, or commit the corrected artifact intentionally.

### Scheduled Run Cannot Commit

1. Check workflow permissions include `contents: write` for `scrape-and-generate-rss`.
2. Check branch protection rules for `main`.
3. Check whether generated artifacts are outside the staging allowlist.

### LLM Enrichment Fails

1. Confirm `GH_MODELS_TOKEN` or `GH_Models_Token` exists.
2. Check rate-limit or model error details in pipeline logs.
3. Confirm degraded mode still publishes ranked non-LLM output.
4. Review `reports/pipeline_report.json` for `llm_status`.

### Jekyll Build Fails

1. Run the build locally with the same command shape.
2. Check `_config.yml` excludes for operational folders.
3. Check recently moved docs or generated files for unintended site processing.
4. Check Ruby/Bundler warnings separately from hard build failures.

## Operational Signals

| Signal | Location |
| --- | --- |
| Feed health | `api/rss_status.json` |
| Aggregation source health | `reports/aggregation/*_health.json` |
| Aggregation reports | `reports/aggregation/*_report.md` |
| Pipeline report | `reports/pipeline_report.json` and `reports/pipeline_report.md` |
| Fetch telemetry | `derived/fetch_log.jsonl` |
| LLM call telemetry | `derived/llm_call_log.jsonl` |

## Escalation Rules

- Public feed path changes require explicit review.
- New secrets require documentation and degraded-mode behavior.
- New generated artifact paths require workflow staging updates.
- New deploy jobs require concurrency review.
- Any change that modifies committed generated artifacts should include local validation output in the PR or commit notes.
