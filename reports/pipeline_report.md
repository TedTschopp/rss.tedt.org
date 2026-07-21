# Pipeline Report

- Timestamp: 2026-07-21T01:56:37.902605Z
- Sources configured: 43
- Raw items: 1870
- Stories: 1815
- Clusters: 1785
- LLM: {'status': 'degraded', 'calls': 113, 'ok': 112, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 102, 'ok': 101, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 102}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 113
- Enrichment: 11
- Publish: 102

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 6.31
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 17.22
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 507.92
- persist_llm_cache: 0.21