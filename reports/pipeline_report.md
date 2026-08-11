# Pipeline Report

- Timestamp: 2026-08-11T08:32:15.578293Z
- Sources configured: 43
- Raw items: 1832
- Stories: 1800
- Clusters: 1773
- LLM: {'status': 'degraded', 'calls': 103, 'ok': 101, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 29, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 92, 'ok': 90, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 29, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 92}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 103
- Enrichment: 11
- Publish: 92

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.74
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 24.46
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 641.74
- persist_llm_cache: 0.21