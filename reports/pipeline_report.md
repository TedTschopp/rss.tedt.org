# Pipeline Report

- Timestamp: 2026-07-08T17:27:58.978854Z
- Sources configured: 43
- Raw items: 1849
- Stories: 1798
- Clusters: 1795
- LLM: {'status': 'degraded', 'calls': 121, 'ok': 120, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 10, 'ok': 10, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 111, 'ok': 110, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 111}}}}

## LLM Calls
- Total: 121
- Enrichment: 10
- Publish: 111

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.19
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 17.11
- cluster: 1.68
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 381.98
- persist_llm_cache: 2.54