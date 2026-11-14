# Pipeline Report

- Timestamp: 2026-11-14T20:37:55.077097Z
- Sources configured: 43
- Raw items: 2178
- Stories: 2133
- Clusters: 2104
- LLM: {'status': 'degraded', 'calls': 99, 'ok': 97, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 39, 'importance': 29, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 88, 'ok': 86, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 39, 'importance': 29, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 88}, 'backlog': {'ai_relevance': {'before': 39, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 39, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 99
- Enrichment: 11
- Publish: 88

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.39
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 12.74
- cluster: 0.14
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 383.66
- persist_llm_cache: 0.23