# Pipeline Report

- Timestamp: 2026-07-26T08:55:20.545829Z
- Sources configured: 43
- Raw items: 1806
- Stories: 1764
- Clusters: 1735
- LLM: {'status': 'degraded', 'calls': 112, 'ok': 111, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 35, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 101, 'ok': 100, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 35, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 101}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 112
- Enrichment: 11
- Publish: 101

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.68
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 19.57
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 410.85
- persist_llm_cache: 0.21