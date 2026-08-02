# Pipeline Report

- Timestamp: 2026-08-02T00:35:01.345894Z
- Sources configured: 43
- Raw items: 1942
- Stories: 1885
- Clusters: 1856
- LLM: {'status': 'degraded', 'calls': 127, 'ok': 124, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 116, 'ok': 113, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 116}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 127
- Enrichment: 11
- Publish: 116

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.51
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 15.11
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 516.76
- persist_llm_cache: 0.21