# Pipeline Report

- Timestamp: 2026-09-26T16:11:21.775722Z
- Sources configured: 43
- Raw items: 2077
- Stories: 2024
- Clusters: 1996
- LLM: {'status': 'degraded', 'calls': 124, 'ok': 123, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 42, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 113, 'ok': 112, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 42, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 113}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 124
- Enrichment: 11
- Publish: 113

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.50
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 14.87
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 289.53
- persist_llm_cache: 0.22