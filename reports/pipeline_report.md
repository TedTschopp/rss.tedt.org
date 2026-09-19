# Pipeline Report

- Timestamp: 2026-09-19T03:51:45.518697Z
- Sources configured: 43
- Raw items: 1978
- Stories: 1923
- Clusters: 1892
- LLM: {'status': 'degraded', 'calls': 238, 'ok': 237, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 107, 'importance': 62, 'output_cleanup': 43}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'degraded', 'calls': 212, 'ok': 211, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 107, 'importance': 62, 'output_cleanup': 43}, 'by_model': {'openai/gpt-4.1-mini': 212}, 'backlog': {'ai_relevance': {'before': 107, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 107, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 238
- Enrichment: 26
- Publish: 212

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.33
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 29.73
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 571.28
- persist_llm_cache: 0.13