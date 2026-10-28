# Pipeline Report

- Timestamp: 2026-10-28T16:13:33.403987Z
- Sources configured: 43
- Raw items: 2244
- Stories: 2187
- Clusters: 2161
- LLM: {'status': 'degraded', 'calls': 132, 'ok': 129, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 121, 'ok': 118, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 121}, 'backlog': {'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 132
- Enrichment: 11
- Publish: 121

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.64
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 18.37
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 480.48
- persist_llm_cache: 0.22