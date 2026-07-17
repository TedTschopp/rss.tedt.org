# Pipeline Report

- Timestamp: 2026-07-17T17:09:36.327395Z
- Sources configured: 43
- Raw items: 1846
- Stories: 1798
- Clusters: 1766
- LLM: {'status': 'degraded', 'calls': 124, 'ok': 123, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 113, 'ok': 112, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 113}, 'backlog': {'ai_relevance': {'before': 54, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 54, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 124
- Enrichment: 11
- Publish: 113

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.93
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 24.70
- cluster: 0.19
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 433.52
- persist_llm_cache: 0.17