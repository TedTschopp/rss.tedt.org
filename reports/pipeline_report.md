# Pipeline Report

- Timestamp: 2026-11-19T17:20:10.106871Z
- Sources configured: 43
- Raw items: 2170
- Stories: 2137
- Clusters: 2109
- LLM: {'status': 'degraded', 'calls': 171, 'ok': 170, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 60, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 160, 'ok': 159, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 60, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 160}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 171
- Enrichment: 11
- Publish: 160

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.29
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 20.39
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 577.48
- persist_llm_cache: 0.27