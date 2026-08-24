# Pipeline Report

- Timestamp: 2026-08-24T16:21:33.020577Z
- Sources configured: 43
- Raw items: 2045
- Stories: 2012
- Clusters: 1983
- LLM: {'status': 'degraded', 'calls': 123, 'ok': 120, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 36, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 112, 'ok': 109, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 36, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 112}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 123
- Enrichment: 11
- Publish: 112

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.48
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 22.32
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 593.26
- persist_llm_cache: 0.21