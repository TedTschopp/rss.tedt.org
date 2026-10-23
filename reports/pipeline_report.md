# Pipeline Report

- Timestamp: 2026-10-23T16:11:18.639811Z
- Sources configured: 43
- Raw items: 2178
- Stories: 2119
- Clusters: 2090
- LLM: {'status': 'degraded', 'calls': 113, 'ok': 112, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 35, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 102, 'ok': 101, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 35, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 102}, 'backlog': {'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

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
- ingestion: 2.02
- normalize: 0.09
- dedupe: 0.07
- llm_enrich: 15.48
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 291.27
- persist_llm_cache: 0.23