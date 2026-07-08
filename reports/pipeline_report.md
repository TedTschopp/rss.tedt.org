# Pipeline Report

- Timestamp: 2026-07-08T10:17:44.250880Z
- Sources configured: 43
- Raw items: 1801
- Stories: 1747
- Clusters: 1745
- LLM: {'status': 'degraded', 'calls': 112, 'ok': 111, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 101, 'ok': 100, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 101}}}}

## LLM Calls
- Total: 112
- Enrichment: 11
- Publish: 101

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.86
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 23.04
- cluster: 2.00
- score: 0.01
- write_intermediate_outputs: 0.23
- publish: 496.48
- persist_llm_cache: 2.91