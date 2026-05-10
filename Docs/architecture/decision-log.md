# Architecture Decision Log

This log captures durable decisions that affect repo structure, automation, public URLs, and extension behavior.

## ADR-001: Keep Public Feed Outputs Path-Stable

**Status:** Accepted

**Decision:** Public feed outputs remain at their published root or `feeds/` paths.

**Rationale:** External systems may subscribe directly to feed URLs. Moving feed outputs is a breaking change even if the code still works.

**Implications:** New public feeds need intentional names. Internal state belongs in `derived/` or `reports/`, not root.

## ADR-002: Use `scripts/` For Python Entrypoints

**Status:** Accepted

**Decision:** Python entrypoints run as modules under `scripts/`, for example `python -m scripts.enhanced_scraper`.

**Rationale:** Root-level scripts mixed operational code with public web artifacts. The module pattern gives a clearer ownership boundary.

**Implications:** Workflow commands and docs should use module invocation. Imports shared with the pipeline should be package-qualified.

## ADR-003: Move Site Status To `api/rss_status.json`

**Status:** Accepted

**Decision:** Feed health status is generated at `api/rss_status.json` and fetched by site pages from `/api/rss_status.json`.

**Rationale:** The site uses the status payload, but external subscribers are not expected to rely on root `rss_status.json`.

**Implications:** The monitor, site fetches, validators, and workflow staging must all agree on the `api/` path.

## ADR-004: Keep Operational State Out Of The Public Root

**Status:** Accepted

**Decision:** Internal state and reports live under `derived/` and `reports/`.

**Rationale:** Generated state such as caches, skip lists, and health reports supports the pipeline but should not clutter the public root namespace.

**Implications:** New generated artifacts must have an owner and be staged by workflow allowlist when they need to persist.

## ADR-005: Use `Docs/` As The Durable Documentation Root

**Status:** Accepted

**Decision:** Product, architecture, operations, design, setup, reference, and archive docs live under `Docs/`.

**Rationale:** The repo needs documentation that can grow without competing with public GitHub Pages root files.

**Implications:** `Docs/` is excluded from Jekyll processing. Code may depend on stable files under `Docs/reference/`, so reference docs require extra care.

## ADR-006: Keep `New-Home/` Isolated Until Promotion

**Status:** Accepted

**Decision:** `New-Home/` remains an isolated redesign/template workspace.

**Rationale:** The site is evolving beyond RSS, but the redesign should not be blended into production paths until templates, data contracts, and rollback are clear.

**Implications:** Promotion requires an explicit plan, validation, and URL impact review.

## ADR-007: Validate Workflow And Path Contracts Locally

**Status:** Accepted

**Decision:** Add a lightweight workflow/path validator and standard-library tests.

**Rationale:** Most likely failures are path and artifact-contract regressions, not complex algorithmic bugs.

**Implications:** Pipeline changes should run `python -m scripts.validate_workflow` and `python -m unittest discover -s tests` before push.
