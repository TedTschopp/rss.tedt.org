# Pipeline Report

- Timestamp: 2026-09-17T04:00:27.975870Z
- Sources configured: 43
- Raw items: 3254
- Stories: 2470
- Clusters: 2439
- LLM: {'status': 'ok', 'calls': 401, 'ok': 401, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 170, 'importance': 160, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'ok', 'calls': 375, 'ok': 375, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 170, 'importance': 160, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 375}, 'backlog': {'ai_relevance': {'before': 170, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 170, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 401
- Enrichment: 26
- Publish: 375

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.95
- normalize: 0.12
- dedupe: 0.07
- llm_enrich: 28.17
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.33
- publish: 1043.93
- persist_llm_cache: 0.18