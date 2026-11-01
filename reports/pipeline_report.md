# Pipeline Report

- Timestamp: 2026-11-01T14:44:52.474686Z
- Sources configured: 43
- Raw items: 2140
- Stories: 2096
- Clusters: 2069
- LLM: {'status': 'degraded', 'calls': 116, 'ok': 114, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 35, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 105, 'ok': 103, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 35, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 105}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 50, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 116
- Enrichment: 11
- Publish: 105

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 4.60
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 13.17
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 339.66
- persist_llm_cache: 0.26