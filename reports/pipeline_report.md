# Pipeline Report

- Timestamp: 2026-09-07T16:14:05.896813Z
- Sources configured: 43
- Raw items: 1893
- Stories: 1859
- Clusters: 1831
- LLM: {'status': 'degraded', 'calls': 114, 'ok': 111, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 37, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 103, 'ok': 100, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 37, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 103}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 114
- Enrichment: 11
- Publish: 103

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.60
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 15.60
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 485.86
- persist_llm_cache: 0.20