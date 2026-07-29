# Pipeline Report

- Timestamp: 2026-07-29T16:43:08.175461Z
- Sources configured: 43
- Raw items: 1926
- Stories: 1870
- Clusters: 1843
- LLM: {'status': 'degraded', 'calls': 162, 'ok': 159, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 61, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 151, 'ok': 148, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 61, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 151}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 162
- Enrichment: 11
- Publish: 151

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.57
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 17.76
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 729.49
- persist_llm_cache: 0.21