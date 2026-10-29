# Pipeline Report

- Timestamp: 2026-10-29T00:18:10.633132Z
- Sources configured: 43
- Raw items: 2191
- Stories: 2130
- Clusters: 2104
- LLM: {'status': 'degraded', 'calls': 166, 'ok': 165, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 62, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 155, 'ok': 154, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 62, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 155}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 166
- Enrichment: 11
- Publish: 155

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.28
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 16.18
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 469.43
- persist_llm_cache: 0.22