# Pipeline Report

- Timestamp: 2026-10-29T08:15:47.375075Z
- Sources configured: 43
- Raw items: 2531
- Stories: 2497
- Clusters: 2471
- LLM: {'status': 'degraded', 'calls': 184, 'ok': 183, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 173, 'ok': 172, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 173}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 184
- Enrichment: 11
- Publish: 173

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.31
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 14.64
- cluster: 0.23
- score: 0.03
- write_intermediate_outputs: 0.33
- publish: 563.51
- persist_llm_cache: 0.28