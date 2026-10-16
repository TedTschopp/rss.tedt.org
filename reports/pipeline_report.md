# Pipeline Report

- Timestamp: 2026-10-16T16:11:35.519000Z
- Sources configured: 43
- Raw items: 2153
- Stories: 2108
- Clusters: 2080
- LLM: {'status': 'degraded', 'calls': 123, 'ok': 122, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 40, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 112, 'ok': 111, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 40, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 112}, 'backlog': {'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 123
- Enrichment: 11
- Publish: 112

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.45
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 17.64
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 305.61
- persist_llm_cache: 0.21