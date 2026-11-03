# Pipeline Report

- Timestamp: 2026-11-03T16:09:13.828789Z
- Sources configured: 43
- Raw items: 6276
- Stories: 4117
- Clusters: 4089
- LLM: {'status': 'degraded', 'calls': 187, 'ok': 185, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 176, 'ok': 174, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 176}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 187
- Enrichment: 11
- Publish: 176

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.73
- normalize: 0.26
- dedupe: 0.12
- llm_enrich: 17.11
- cluster: 0.19
- score: 0.03
- write_intermediate_outputs: 0.50
- publish: 704.51
- persist_llm_cache: 0.17