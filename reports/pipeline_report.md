# Pipeline Report

- Timestamp: 2026-11-16T18:18:55.624210Z
- Sources configured: 43
- Raw items: 2272
- Stories: 2214
- Clusters: 2186
- LLM: {'status': 'degraded', 'calls': 155, 'ok': 150, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 56, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 144, 'ok': 139, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 56, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 144}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 5}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 68, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 15}

## LLM Calls
- Total: 155
- Enrichment: 11
- Publish: 144

## Enrichment Backlog
- Remaining: 15
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.38
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 17.81
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 847.53
- persist_llm_cache: 0.26