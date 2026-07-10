# Pipeline Report

- Timestamp: 2026-07-10T02:08:36.344047Z
- Sources configured: 43
- Raw items: 2898
- Stories: 2263
- Clusters: 2259
- LLM: {'status': 'degraded', 'calls': 137, 'ok': 136, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 126, 'ok': 125, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 126}}}}

## LLM Calls
- Total: 137
- Enrichment: 11
- Publish: 126

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 10.61
- normalize: 0.14
- dedupe: 0.08
- llm_enrich: 20.25
- cluster: 3.53
- score: 0.01
- write_intermediate_outputs: 0.35
- publish: 493.75
- persist_llm_cache: 3.06