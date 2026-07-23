# Pipeline Report

- Timestamp: 2026-07-23T00:33:52.070153Z
- Sources configured: 43
- Raw items: 1882
- Stories: 1819
- Clusters: 1791
- LLM: {'status': 'degraded', 'calls': 129, 'ok': 126, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 42, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 118, 'ok': 115, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 42, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 118}, 'backlog': {'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 129
- Enrichment: 11
- Publish: 118

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.71
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 16.04
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 502.48
- persist_llm_cache: 0.21