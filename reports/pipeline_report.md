# Pipeline Report

- Timestamp: 2026-10-14T16:13:29.930158Z
- Sources configured: 43
- Raw items: 2155
- Stories: 2102
- Clusters: 2075
- LLM: {'status': 'degraded', 'calls': 160, 'ok': 159, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 57, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 149, 'ok': 148, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 57, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 149}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 160
- Enrichment: 11
- Publish: 149

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.50
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 13.52
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.31
- publish: 401.45
- persist_llm_cache: 0.27