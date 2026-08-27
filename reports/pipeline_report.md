# Pipeline Report

- Timestamp: 2026-08-27T19:42:39.210933Z
- Sources configured: 43
- Raw items: 2010
- Stories: 1946
- Clusters: 1918
- LLM: {'status': 'degraded', 'calls': 150, 'ok': 149, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 139, 'ok': 138, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 139}, 'backlog': {'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 150
- Enrichment: 11
- Publish: 139

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.43
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 17.77
- cluster: 0.22
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 595.66
- persist_llm_cache: 0.16