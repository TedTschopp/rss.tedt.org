# Pipeline Report

- Timestamp: 2026-11-20T06:20:40.026801Z
- Sources configured: 43
- Raw items: 4253
- Stories: 3293
- Clusters: 3265
- LLM: {'status': 'degraded', 'calls': 189, 'ok': 187, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 178, 'ok': 176, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 178}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 189
- Enrichment: 11
- Publish: 178

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.30
- normalize: 0.23
- dedupe: 0.12
- llm_enrich: 15.83
- cluster: 0.26
- score: 0.04
- write_intermediate_outputs: 0.50
- publish: 740.48
- persist_llm_cache: 0.27