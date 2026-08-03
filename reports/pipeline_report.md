# Pipeline Report

- Timestamp: 2026-08-03T09:18:06.105733Z
- Sources configured: 43
- Raw items: 3234
- Stories: 2308
- Clusters: 2280
- LLM: {'status': 'ok', 'calls': 189, 'ok': 189, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 178, 'ok': 178, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 178}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 189
- Enrichment: 11
- Publish: 178

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.20
- normalize: 0.18
- dedupe: 0.09
- llm_enrich: 17.80
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.38
- publish: 779.84
- persist_llm_cache: 0.21