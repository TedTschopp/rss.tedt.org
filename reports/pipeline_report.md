# Pipeline Report

- Timestamp: 2026-09-26T08:16:59.955776Z
- Sources configured: 43
- Raw items: 2276
- Stories: 2245
- Clusters: 2217
- LLM: {'status': 'degraded', 'calls': 183, 'ok': 182, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 172, 'ok': 171, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 172}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 183
- Enrichment: 11
- Publish: 172

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.81
- normalize: 0.10
- dedupe: 0.07
- llm_enrich: 12.96
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 557.35
- persist_llm_cache: 0.22