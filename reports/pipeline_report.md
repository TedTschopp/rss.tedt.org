# Pipeline Report

- Timestamp: 2026-10-15T04:00:56.267326Z
- Sources configured: 43
- Raw items: 7442
- Stories: 4554
- Clusters: 4523
- LLM: {'status': 'degraded', 'calls': 391, 'ok': 390, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 159, 'ai_relevance': 162, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'degraded', 'calls': 365, 'ok': 364, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 159, 'ai_relevance': 162, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 365}, 'backlog': {'ai_relevance': {'before': 162, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 162, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 391
- Enrichment: 26
- Publish: 365

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 6.43
- normalize: 0.27
- dedupe: 0.13
- llm_enrich: 29.09
- cluster: 0.20
- score: 0.03
- write_intermediate_outputs: 0.65
- publish: 993.47
- persist_llm_cache: 0.22