# Pipeline Report

- Timestamp: 2026-10-22T08:15:11.000166Z
- Sources configured: 43
- Raw items: 4339
- Stories: 3539
- Clusters: 3512
- LLM: {'status': 'ok', 'calls': 169, 'ok': 169, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 68, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 158, 'ok': 158, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 68, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 158}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 169
- Enrichment: 11
- Publish: 158

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.45
- normalize: 0.13
- dedupe: 0.07
- llm_enrich: 16.13
- cluster: 0.17
- score: 0.02
- write_intermediate_outputs: 0.43
- publish: 441.51
- persist_llm_cache: 0.25