# Pipeline Report

- Timestamp: 2026-10-18T08:11:43.743113Z
- Sources configured: 43
- Raw items: 2026
- Stories: 1990
- Clusters: 1962
- LLM: {'status': 'degraded', 'calls': 91, 'ok': 90, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 23, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 80, 'ok': 79, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 23, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 80}, 'backlog': {'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 91
- Enrichment: 11
- Publish: 80

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.71
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 12.63
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 291.66
- persist_llm_cache: 0.22