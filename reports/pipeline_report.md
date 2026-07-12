# Pipeline Report

- Timestamp: 2026-07-12T01:56:48.159330Z
- Sources configured: 43
- Raw items: 1846
- Stories: 1803
- Clusters: 1798
- LLM: {'status': 'degraded', 'calls': 97, 'ok': 96, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 21, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 86, 'ok': 85, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 21, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 86}}}}

## LLM Calls
- Total: 97
- Enrichment: 11
- Publish: 86

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.86
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 19.60
- cluster: 2.63
- score: 0.01
- write_intermediate_outputs: 0.23
- publish: 373.31
- persist_llm_cache: 3.34