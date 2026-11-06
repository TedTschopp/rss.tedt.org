# Pipeline Report

- Timestamp: 2026-11-06T11:35:37.486567Z
- Sources configured: 43
- Raw items: 2134
- Stories: 2077
- Clusters: 2048
- LLM: {'status': 'degraded', 'calls': 241, 'ok': 240, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 91, 'importance': 74, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}}}, 'publish': {'status': 'degraded', 'calls': 215, 'ok': 214, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 91, 'importance': 74, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 215}, 'backlog': {'ai_relevance': {'before': 91, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}, 'ai_relevance': {'before': 91, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 24}

## LLM Calls
- Total: 241
- Enrichment: 26
- Publish: 215

## Enrichment Backlog
- Remaining: 24
- embeddings: 0
- summaries: 23
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.79
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 29.77
- cluster: 0.16
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 756.98
- persist_llm_cache: 0.16