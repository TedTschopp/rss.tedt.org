# Pipeline Report

- Timestamp: 2026-08-23T00:13:36.403874Z
- Sources configured: 43
- Raw items: 1961
- Stories: 1913
- Clusters: 1884
- LLM: {'status': 'ok', 'calls': 114, 'ok': 114, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 103, 'ok': 103, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 103}, 'backlog': {'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 114
- Enrichment: 11
- Publish: 103

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.58
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 15.77
- cluster: 0.21
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 314.80
- persist_llm_cache: 0.14