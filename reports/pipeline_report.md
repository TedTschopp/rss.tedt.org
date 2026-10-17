# Pipeline Report

- Timestamp: 2026-10-17T08:14:29.780679Z
- Sources configured: 43
- Raw items: 2464
- Stories: 2415
- Clusters: 2387
- LLM: {'status': 'degraded', 'calls': 173, 'ok': 172, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 70, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 162, 'ok': 161, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 70, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 162}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 173
- Enrichment: 11
- Publish: 162

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.18
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 11.88
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 467.14
- persist_llm_cache: 0.26