# Pipeline Report

- Timestamp: 2026-11-19T12:22:48.996260Z
- Sources configured: 43
- Raw items: 2158
- Stories: 2123
- Clusters: 2095
- LLM: {'status': 'degraded', 'calls': 286, 'ok': 285, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 122, 'importance': 88, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}}}, 'publish': {'status': 'degraded', 'calls': 260, 'ok': 259, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 122, 'importance': 88, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 260}, 'backlog': {'ai_relevance': {'before': 122, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}, 'ai_relevance': {'before': 122, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 24}

## LLM Calls
- Total: 286
- Enrichment: 26
- Publish: 260

## Enrichment Backlog
- Remaining: 24
- embeddings: 0
- summaries: 23
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 19.08
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 35.72
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 1219.73
- persist_llm_cache: 0.27