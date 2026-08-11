# Pipeline Report

- Timestamp: 2026-08-11T16:34:21.666740Z
- Sources configured: 43
- Raw items: 1931
- Stories: 1890
- Clusters: 1863
- LLM: {'status': 'degraded', 'calls': 166, 'ok': 162, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 61, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 155, 'ok': 151, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 61, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 155}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 166
- Enrichment: 11
- Publish: 155

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.97
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 58.12
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 856.44
- persist_llm_cache: 0.21