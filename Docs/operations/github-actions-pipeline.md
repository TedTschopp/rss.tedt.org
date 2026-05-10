# GitHub Actions Pipeline

## Purpose

The GitHub Actions workflow is the operating backbone for `rss.tedt.org`. It refreshes feed data, commits generated artifacts, and deploys the static site to GitHub Pages.

The workflow file is [.github/workflows/scrape-and-generate-rss.yml](../../.github/workflows/scrape-and-generate-rss.yml).

## Triggers

| Trigger | What Happens |
| --- | --- |
| Schedule: `0 */8 * * *` | Runs the scraper, ranking pipeline, monitor, artifact commit step, then deploys Pages. |
| `workflow_dispatch` | Same as schedule, but manually triggered. |
| Push to `main` | Deploys the Jekyll site for human-authored repo changes. It does not run scraping. |

## Job Map

| Job | Runs On | Trigger Condition | Responsibility |
| --- | --- | --- | --- |
| `scrape-and-generate-rss` | `ubuntu-latest` | Any non-push event | Refresh data, generate artifacts, commit generated outputs. |
| `deploy-on-push` | `ubuntu-latest` | Human push to `main` | Build and deploy the Jekyll site. |
| `deploy-after-scrape` | `ubuntu-latest` | Always after scheduled/manual scrape | Build and deploy latest `main`, even if scraping had warnings or partial failure. |

## Scrape And Generate Job

### Step Sequence

1. Check out the repository.
2. Set up Python 3.13.
3. Install Python dependencies from `requirements.txt`.
4. Install Playwright Chromium dependencies.
5. Run `python -m scripts.enhanced_scraper`.
6. Run `python -m pipeline.run_all`.
7. Run `python -m scripts.monitor`.
8. Stage generated artifacts by allowlist.
9. Commit and push generated artifacts if anything changed.

### Inputs

| Input | Source | Used By |
| --- | --- | --- |
| `_config.yml` | Repo | Aggregated feed configuration and Jekyll settings. |
| `sources.yml` | Repo | Top Stories source registry and ranking settings. |
| `requirements.txt` | Repo | Python runtime dependencies. |
| `GH_MODELS_TOKEN` or `GH_Models_Token` | GitHub secret | Optional LLM enrichment and importance tagging. |

### Outputs

| Output | Location | Public Contract |
| --- | --- | --- |
| Primary AI feed | `ai_rss_feed.xml`, `ai_rss_feed.atom`, `ai_rss_feed.json`, `ai_rss_feed_rss1.xml` | Yes |
| Aggregated feeds | `aggregated_*.xml`, `aggregated_*.atom`, `aggregated_*.json`, `aggregated_*_rss1.xml` | Yes |
| Feed archives | `*_archive.xml` | Yes where present |
| Top Stories feed | `feeds/top.xml`, `feeds/top.atom`, `feeds/top.json`, `feeds/top_rss1.xml` | Yes |
| Site status | `api/rss_status.json` | Used by site pages |
| API feed | `api/feed.json` | Public API output |
| Pipeline data | `data/*.json`, `derived/*.json`, `derived/*.jsonl` | Repo operational artifacts |
| Reports | `reports/*.json`, `reports/*.md`, `reports/aggregation/*` | Repo operational artifacts |

## Deployment Jobs

Both deployment jobs use the same deployment model:

1. Check out `main`.
2. Set up Ruby 3.2 with Bundler cache.
3. Configure GitHub Pages.
4. Run `bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"`.
5. Upload `_site` as a Pages artifact.
6. Deploy with `actions/deploy-pages@v4`.

The difference is trigger intent:

- `deploy-on-push` handles human changes to the site or repo.
- `deploy-after-scrape` handles scheduled/manual data refreshes after the generated artifacts are committed.

## Artifact Commit Model

The workflow stages generated artifacts by allowlist:

```bash
*rss_feed*.xml
*rss_feed*.atom
*rss_feed*.json
aggregated*.xml
aggregated*.atom
aggregated*.json
api/*.json
feeds/*
data/*.json
derived/*.json
derived/*.jsonl
reports/*.json
reports/*.md
reports/aggregation/*.json
reports/aggregation/*.md
```

If you add a new generated artifact path, add it to this allowlist or it will not be committed by scheduled/manual runs.

## Failure Behavior

| Failure | Expected Behavior |
| --- | --- |
| No feed changes | Job exits successfully and does not commit. |
| Missing LLM token | Pipeline runs in degraded mode where possible. |
| Missing archive feed | Monitor treats missing archives as informational until retention creates them. |
| Monitor warning | Workflow continues unless overall status is `error`. |
| Scrape job failure | `deploy-after-scrape` still attempts to deploy latest `main`. |
| Human push by `github-actions[bot]` | Deploy-on-push is skipped to avoid loops. |

## Local Validation Commands

Run these before changing the workflow or pipeline contract:

```bash
source .venv/bin/activate
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_workflow
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/config.py scripts/feed_generator.py scripts/enhanced_scraper.py scripts/scrape_to_rss.py scripts/monitor.py scripts/validate_setup.py pipeline/publish.py
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_setup
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.monitor
bundle exec jekyll build --destination /tmp/rss-tedt-actions-build
```

If `actionlint` is installed, also run:

```bash
actionlint .github/workflows/scrape-and-generate-rss.yml
```

`actionlint` is optional local tooling today. If it is not installed, the repository validator still checks workflow structure, required jobs, key commands, and artifact staging globs.

## Current Constraints

- Public feed paths are intentionally root-level and should not be moved casually.
- GitHub Actions is the production refresh path, not just a test harness.
- Generated artifacts are committed to `main`, so workflow changes can create repository churn quickly.
- Linux Actions runners are case-sensitive. Match `Docs/`, `scripts/`, and file names exactly.
