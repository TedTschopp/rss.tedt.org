# Pipeline Report

- Timestamp: 2026-09-02T00:22:26.846937Z
- Sources configured: 43
- Raw items: 2017
- Stories: 1956
- Clusters: 1927
- LLM: {'status': 'ok', 'calls': 149, 'ok': 149, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 49, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 138, 'ok': 138, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 49, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 138}, 'backlog': {'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 149
- Enrichment: 11
- Publish: 138

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.80
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 21.37
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.31
- publish: 535.81
- persist_llm_cache: 0.19