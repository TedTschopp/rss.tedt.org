# Pipeline Report

- Timestamp: 2026-09-21T16:16:54.498620Z
- Sources configured: 43
- Raw items: 2071
- Stories: 2018
- Clusters: 1990
- LLM: {'status': 'degraded', 'calls': 162, 'ok': 160, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 59, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 151, 'ok': 149, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 59, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 151}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 162
- Enrichment: 11
- Publish: 151

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.99
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 22.93
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 607.93
- persist_llm_cache: 0.20