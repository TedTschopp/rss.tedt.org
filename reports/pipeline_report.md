# Pipeline Report

- Timestamp: 2026-07-24T00:35:10.437729Z
- Sources configured: 43
- Raw items: 1910
- Stories: 1857
- Clusters: 1828
- LLM: {'status': 'degraded', 'calls': 141, 'ok': 135, 'errors': 6, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 51, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 130, 'ok': 124, 'errors': 6, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 51, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 130}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 6}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 141
- Enrichment: 11
- Publish: 130

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 5
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.50
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 15.32
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 706.82
- persist_llm_cache: 0.21