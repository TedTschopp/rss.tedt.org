# Pipeline Report

- Timestamp: 2026-10-26T16:19:34.449016Z
- Sources configured: 43
- Raw items: 2197
- Stories: 2142
- Clusters: 2114
- LLM: {'status': 'degraded', 'calls': 167, 'ok': 164, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 61, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 156, 'ok': 153, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 61, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 156}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 167
- Enrichment: 11
- Publish: 156

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 29.31
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.33
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 581.24
- persist_llm_cache: 0.22