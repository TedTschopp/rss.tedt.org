# Pipeline Report

- Timestamp: 2026-07-09T02:11:29.669813Z
- Sources configured: 43
- Raw items: 3047
- Stories: 2372
- Clusters: 2368
- LLM: {'status': 'degraded', 'calls': 110, 'ok': 109, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 38, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 10, 'ok': 10, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 100, 'ok': 99, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 38, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 100}}}}

## LLM Calls
- Total: 110
- Enrichment: 10
- Publish: 100

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.75
- normalize: 0.17
- dedupe: 0.08
- llm_enrich: 27.70
- cluster: 3.53
- score: 0.01
- write_intermediate_outputs: 0.36
- publish: 575.91
- persist_llm_cache: 3.01