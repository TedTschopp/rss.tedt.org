# Documentation Home

This folder is the durable documentation root for the repository. It is organized so product, operations, architecture, design, setup, reference, and archive material can grow without turning the repo root into a filing cabinet.

## Folder Model

| Area | Purpose | Examples |
| --- | --- | --- |
| `architecture/` | System shape, data contracts, integration boundaries, architectural decisions. | Pipeline architecture, data contracts, public URL contracts. |
| `operations/` | How the system runs, how to extend it, and how to recover it. | GitHub Actions pipeline, runbooks, validation procedures. |
| `product/` | Product intent, user journeys, feature framing, roadmap notes. | Site evolution beyond RSS, curated intelligence workflows. |
| `design/` | Experience design, template direction, visual system notes. | `New-Home` redesign, page templates, design-system decisions. |
| `reference/` | Stable reference material used by humans or code. | Importance rubrics, source lists, taxonomies. |
| `setup/` | Setup and deployment instructions. | Jekyll and deployment setup notes. |
| `archive/` | Historical notes retained for context. | Launch notes and older README variants. |

## Start Here

- [GitHub Actions Pipeline](operations/github-actions-pipeline.md) explains the current automation end to end.
- [GitHub Actions Extension Guide](operations/github-actions-extension-guide.md) explains how to change the pipeline without breaking feed URLs or generated artifacts.
- [GitHub Actions Runbook](operations/github-actions-runbook.md) covers routine operation and failure recovery.
- [Pipeline Extension Implementation Plan](operations/pipeline-extension-plan.md) tracks the current hardening plan and validation order.
- [GitHub Actions Pipeline Architecture](architecture/github-actions-pipeline-architecture.md) shows component boundaries and extension points.
- [Public URL Contracts](architecture/public-url-contracts.md) defines which paths are compatibility contracts.
- [Generated Artifact Ownership](architecture/generated-artifact-ownership.md) maps generated files to pipeline owners and staging behavior.
- [Architecture Decision Log](architecture/decision-log.md) captures durable structural decisions.
- [Natural20 Pipeline Architecture](architecture/natural20-pipeline-architecture.md) documents the ranking/API pipeline.
- [Data Contracts](architecture/data-contracts.md) documents generated JSON shapes.

## Documentation Principles

- Put operational procedures in `operations/`, not in the root README.
- Put system structure and contracts in `architecture/`.
- Put user-facing intent and future capability framing in `product/`.
- Put visual and interaction decisions in `design/`.
- Keep `reference/` stable because code may depend on files there.
- Keep `archive/` historical. Do not treat archived notes as current operating truth unless they are refreshed.
