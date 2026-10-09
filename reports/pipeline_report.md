# Pipeline Report

- Timestamp: 2026-10-09T00:20:05.207046Z
- Sources configured: 43
- Raw items: 2095
- Stories: 2037
- Clusters: 2008
- LLM: {'status': 'degraded', 'calls': 142, 'ok': 141, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 50, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 131, 'ok': 130, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 50, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 131}, 'backlog': {'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 142
- Enrichment: 11
- Publish: 131

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.87
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.29
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 377.18
- persist_llm_cache: 0.22