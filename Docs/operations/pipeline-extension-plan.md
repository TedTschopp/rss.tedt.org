# Pipeline Extension Implementation Plan

## Purpose

This plan tracks the next hardening pass for `rss.tedt.org`. The goal is to make the GitHub Actions pipeline easier to extend without breaking public feed URLs, generated artifact commits, or site-facing JSON contracts.

If work stops midway, restart here.

## Guiding Principles

- Public URL contracts are architecture, not housekeeping.
- GitHub Actions is production infrastructure for this repository.
- Generated artifacts must have explicit ownership and staging behavior.
- Validation should catch path and workflow mistakes before a scheduled run does.
- `New-Home/` stays isolated until there is an intentional promotion path.
- Current operating documentation lives under `Docs/`; historical notes live under `Docs/archive/`.

## Ordered Work Plan

| Order | Work Item | Output | Status |
| --- | --- | --- | --- |
| 1 | Capture durable plan | `Docs/operations/pipeline-extension-plan.md` | Complete |
| 2 | Document public URL contracts | `Docs/architecture/public-url-contracts.md` | Complete |
| 3 | Document architecture decisions | `Docs/architecture/decision-log.md` | Complete |
| 4 | Document artifact ownership | `Docs/architecture/generated-artifact-ownership.md` | Complete |
| 5 | Formalize data contract policy | Update `Docs/architecture/data-contracts.md` | Complete |
| 6 | Document `New-Home` promotion path | `Docs/product/new-home-promotion-plan.md` | Complete |
| 7 | Add archived-doc banners | `Docs/archive/*.md` | Complete |
| 8 | Add workflow validation script | `scripts/validate_workflow.py` | Complete |
| 9 | Add path-contract tests | `tests/test_path_contracts.py` | Complete |
| 10 | Update operations docs | Pipeline docs and runbook validation checklists | Complete |
| 11 | Validate all changes | Markdown diagnostics, Python compile, unit tests, setup validator, Jekyll build | Complete |

## Execution Order Rationale

1. **Document contracts before adding controls.** The validator and tests should encode explicit contracts, not guesses.
2. **Add executable validation before broad future changes.** The next pipeline extension should fail fast locally if it breaks path contracts.
3. **Update operational docs after commands exist.** The runbook should reference real scripts and commands.
4. **Validate at the end with the same commands future work will use.** This makes the plan repeatable.

## Validation Commands

Run these after changes in this plan:

```bash
source .venv/bin/activate
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_workflow
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_setup
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/config.py scripts/feed_generator.py scripts/enhanced_scraper.py scripts/scrape_to_rss.py scripts/monitor.py scripts/validate_setup.py scripts/validate_workflow.py pipeline/publish.py
bundle exec jekyll build --destination /tmp/rss-tedt-extension-plan-build
find . -maxdepth 3 \( -name '__pycache__' -o -name '.DS_Store' \) -not -path './.venv/*' -not -path './vendor/*' -print | sort
```

## Open Follow-Ups

- Consider adding `actionlint` to local tooling or CI once the preferred installation method is clear.
- Consider adding schema files for `api/feed.json`, `data/stories.json`, and `api/rss_status.json` if the site evolves beyond static RSS/feed consumption.
- Consider a future PR template section for public URL contract impact.
