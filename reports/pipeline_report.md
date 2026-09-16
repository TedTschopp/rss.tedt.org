# Pipeline Report

- Timestamp: 2026-09-16T16:14:54.711292Z
- Sources configured: 43
- Raw items: 2094
- Stories: 2035
- Clusters: 2005
- LLM: {'status': 'degraded', 'calls': 166, 'ok': 165, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 59, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 155, 'ok': 154, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 59, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 155}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 166
- Enrichment: 11
- Publish: 155

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.56
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 16.29
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 462.65
- persist_llm_cache: 0.17