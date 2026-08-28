# Pipeline Report

- Timestamp: 2026-08-28T20:09:42.344670Z
- Sources configured: 43
- Raw items: 2011
- Stories: 1956
- Clusters: 1928
- LLM: {'status': 'degraded', 'calls': 119, 'ok': 116, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 37, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 108, 'ok': 105, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 37, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 108}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 119
- Enrichment: 11
- Publish: 108

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.19
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 18.19
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 462.51
- persist_llm_cache: 0.21