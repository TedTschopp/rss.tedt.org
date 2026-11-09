# Pipeline Report

- Timestamp: 2026-11-09T05:13:30.982635Z
- Sources configured: 43
- Raw items: 3919
- Stories: 2914
- Clusters: 2885
- LLM: {'status': 'degraded', 'calls': 184, 'ok': 183, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 173, 'ok': 172, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 173}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 184
- Enrichment: 11
- Publish: 173

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.21
- normalize: 0.14
- dedupe: 0.08
- llm_enrich: 20.54
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.44
- publish: 532.38
- persist_llm_cache: 0.27