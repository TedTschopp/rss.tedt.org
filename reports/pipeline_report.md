# Pipeline Report

- Timestamp: 2026-09-09T16:15:50.228378Z
- Sources configured: 43
- Raw items: 2028
- Stories: 1979
- Clusters: 1949
- LLM: {'status': 'degraded', 'calls': 167, 'ok': 166, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 62, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 156, 'ok': 155, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 62, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 156}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 167
- Enrichment: 11
- Publish: 156

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.95
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 18.38
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 571.95
- persist_llm_cache: 0.22