# Pipeline Report

- Timestamp: 2026-10-01T00:22:48.468428Z
- Sources configured: 43
- Raw items: 2075
- Stories: 2017
- Clusters: 1988
- LLM: {'status': 'degraded', 'calls': 155, 'ok': 153, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 57, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 144, 'ok': 142, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 57, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 144}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 155
- Enrichment: 11
- Publish: 144

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.88
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 14.14
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 455.53
- persist_llm_cache: 0.24