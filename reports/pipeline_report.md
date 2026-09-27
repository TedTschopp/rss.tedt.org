# Pipeline Report

- Timestamp: 2026-09-27T03:52:55.417318Z
- Sources configured: 43
- Raw items: 1977
- Stories: 1936
- Clusters: 1908
- LLM: {'status': 'degraded', 'calls': 168, 'ok': 166, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 26, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'degraded', 'calls': 142, 'ok': 140, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 26, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 142}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 18}

## LLM Calls
- Total: 168
- Enrichment: 26
- Publish: 142

## Enrichment Backlog
- Remaining: 18
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.21
- normalize: 0.06
- dedupe: 0.06
- llm_enrich: 29.57
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 437.77
- persist_llm_cache: 0.22