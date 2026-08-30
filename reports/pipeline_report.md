# Pipeline Report

- Timestamp: 2026-08-30T00:21:57.714711Z
- Sources configured: 43
- Raw items: 1932
- Stories: 1886
- Clusters: 1858
- LLM: {'status': 'degraded', 'calls': 106, 'ok': 103, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 31, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 95, 'ok': 92, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 31, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 95}, 'backlog': {'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 106
- Enrichment: 11
- Publish: 95

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.05
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 16.64
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 460.70
- persist_llm_cache: 0.20