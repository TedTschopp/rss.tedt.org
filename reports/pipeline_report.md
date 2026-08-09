# Pipeline Report

- Timestamp: 2026-08-09T08:28:27.501717Z
- Sources configured: 43
- Raw items: 1840
- Stories: 1802
- Clusters: 1775
- LLM: {'status': 'degraded', 'calls': 76, 'ok': 63, 'errors': 13, 'skipped': 0, 'by_kind': {'ai_relevance': 30, 'importance': 15, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 65, 'ok': 52, 'errors': 13, 'skipped': 0, 'by_kind': {'ai_relevance': 30, 'importance': 15, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 65}, 'backlog': {'ai_relevance': {'before': 30, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 13}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 30, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 13}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 23}

## LLM Calls
- Total: 76
- Enrichment: 11
- Publish: 65

## Enrichment Backlog
- Remaining: 23
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 13
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.29
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 20.58
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 845.81
- persist_llm_cache: 0.22