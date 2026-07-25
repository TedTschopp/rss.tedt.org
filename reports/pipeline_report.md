# Pipeline Report

- Timestamp: 2026-07-25T08:48:18.451237Z
- Sources configured: 43
- Raw items: 1829
- Stories: 1795
- Clusters: 1764
- LLM: {'status': 'degraded', 'calls': 90, 'ok': 88, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 36, 'importance': 23, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 79, 'ok': 77, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 36, 'importance': 23, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 79}, 'backlog': {'ai_relevance': {'before': 36, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 36, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 90
- Enrichment: 11
- Publish: 79

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.09
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 14.53
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 432.95
- persist_llm_cache: 0.20