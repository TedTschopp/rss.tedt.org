# Pipeline Report

- Timestamp: 2026-08-31T00:21:23.025100Z
- Sources configured: 43
- Raw items: 1952
- Stories: 1900
- Clusters: 1873
- LLM: {'status': 'degraded', 'calls': 104, 'ok': 101, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 93, 'ok': 90, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 93}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 104
- Enrichment: 11
- Publish: 93

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.26
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 16.05
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 433.26
- persist_llm_cache: 0.20