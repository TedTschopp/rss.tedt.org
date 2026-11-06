# Pipeline Report

- Timestamp: 2026-11-06T15:58:05.900643Z
- Sources configured: 43
- Raw items: 2597
- Stories: 2543
- Clusters: 2514
- LLM: {'status': 'degraded', 'calls': 178, 'ok': 177, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 71, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 167, 'ok': 166, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 71, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 167}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 178
- Enrichment: 11
- Publish: 167

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.51
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 16.28
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.33
- publish: 677.80
- persist_llm_cache: 0.24