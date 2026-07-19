# Pipeline Report

- Timestamp: 2026-07-19T16:56:01.711990Z
- Sources configured: 43
- Raw items: 1878
- Stories: 1834
- Clusters: 1805
- LLM: {'status': 'degraded', 'calls': 131, 'ok': 129, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 43, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 120, 'ok': 118, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 43, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 120}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 131
- Enrichment: 11
- Publish: 120

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.46
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 13.99
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 567.46
- persist_llm_cache: 0.21