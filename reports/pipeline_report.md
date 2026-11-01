# Pipeline Report

- Timestamp: 2026-11-01T00:17:12.820944Z
- Sources configured: 43
- Raw items: 2148
- Stories: 2097
- Clusters: 2070
- LLM: {'status': 'degraded', 'calls': 116, 'ok': 113, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 33, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 105, 'ok': 102, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 33, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 105}, 'backlog': {'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 116
- Enrichment: 11
- Publish: 105

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.85
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 15.53
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 402.10
- persist_llm_cache: 0.21