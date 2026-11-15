# Pipeline Report

- Timestamp: 2026-11-15T15:36:05.815185Z
- Sources configured: 43
- Raw items: 2224
- Stories: 2171
- Clusters: 2143
- LLM: {'status': 'degraded', 'calls': 110, 'ok': 109, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 99, 'ok': 98, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 99}, 'backlog': {'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 110
- Enrichment: 11
- Publish: 99

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.19
- normalize: 0.10
- dedupe: 0.06
- llm_enrich: 15.71
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 452.19
- persist_llm_cache: 0.28