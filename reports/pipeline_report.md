# Pipeline Report

- Timestamp: 2026-10-04T17:27:39.012942Z
- Sources configured: 43
- Raw items: 2092
- Stories: 2042
- Clusters: 2015
- LLM: {'status': 'degraded', 'calls': 111, 'ok': 109, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 100, 'ok': 98, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 100}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 111
- Enrichment: 11
- Publish: 100

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.94
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 16.73
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 325.53
- persist_llm_cache: 0.22