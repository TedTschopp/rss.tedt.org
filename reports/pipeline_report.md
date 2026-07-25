# Pipeline Report

- Timestamp: 2026-07-25T00:35:39.006035Z
- Sources configured: 43
- Raw items: 1854
- Stories: 1804
- Clusters: 1775
- LLM: {'status': 'degraded', 'calls': 134, 'ok': 132, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 45, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 123, 'ok': 121, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 45, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 123}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 134
- Enrichment: 11
- Publish: 123

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.32
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.26
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 547.90
- persist_llm_cache: 0.21