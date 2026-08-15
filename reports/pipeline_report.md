# Pipeline Report

- Timestamp: 2026-08-15T16:13:28.530618Z
- Sources configured: 43
- Raw items: 1978
- Stories: 1930
- Clusters: 1901
- LLM: {'status': 'degraded', 'calls': 132, 'ok': 131, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 121, 'ok': 120, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 121}, 'backlog': {'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 132
- Enrichment: 11
- Publish: 121

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.00
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 18.00
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 506.42
- persist_llm_cache: 0.20