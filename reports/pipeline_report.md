# Pipeline Report

- Timestamp: 2026-09-19T00:20:36.189481Z
- Sources configured: 43
- Raw items: 1738
- Stories: 1684
- Clusters: 1657
- LLM: {'status': 'degraded', 'calls': 140, 'ok': 139, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 49, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 129, 'ok': 128, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 49, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 129}, 'backlog': {'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 140
- Enrichment: 11
- Publish: 129

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 9.92
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 16.16
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 392.81
- persist_llm_cache: 0.20