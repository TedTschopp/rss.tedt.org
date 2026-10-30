# Pipeline Report

- Timestamp: 2026-10-30T00:17:24.482487Z
- Sources configured: 43
- Raw items: 2143
- Stories: 2094
- Clusters: 2068
- LLM: {'status': 'degraded', 'calls': 146, 'ok': 143, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 47, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 135, 'ok': 132, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 47, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 135}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 146
- Enrichment: 11
- Publish: 135

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.76
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 14.30
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 436.43
- persist_llm_cache: 0.23