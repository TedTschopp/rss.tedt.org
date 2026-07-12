# Pipeline Report

- Timestamp: 2026-07-12T06:31:40.240883Z
- Sources configured: 43
- Raw items: 1856
- Stories: 1815
- Clusters: 1813
- LLM: {'status': 'degraded', 'calls': 179, 'ok': 177, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 90, 'importance': 21, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 21, 'ok': 21, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 158, 'ok': 156, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 90, 'importance': 21, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 158}}}}

## LLM Calls
- Total: 179
- Enrichment: 21
- Publish: 158

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.85
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 29.83
- cluster: 2.00
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 691.16
- persist_llm_cache: 2.95