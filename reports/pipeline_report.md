# Pipeline Report

- Timestamp: 2026-09-08T00:19:27.155254Z
- Sources configured: 43
- Raw items: 1972
- Stories: 1925
- Clusters: 1897
- LLM: {'status': 'degraded', 'calls': 115, 'ok': 114, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 104, 'ok': 103, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 104}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 115
- Enrichment: 11
- Publish: 104

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.42
- normalize: 0.05
- dedupe: 0.06
- llm_enrich: 14.70
- cluster: 0.19
- score: 0.01
- write_intermediate_outputs: 0.21
- publish: 380.45
- persist_llm_cache: 0.13