# Pipeline Report

- Timestamp: 2026-08-15T00:14:34.968317Z
- Sources configured: 43
- Raw items: 1966
- Stories: 1916
- Clusters: 1886
- LLM: {'status': 'degraded', 'calls': 104, 'ok': 103, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 93, 'ok': 92, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 93}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 104
- Enrichment: 11
- Publish: 93

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.19
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 14.13
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 390.34
- persist_llm_cache: 0.13