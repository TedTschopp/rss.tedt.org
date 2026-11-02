# Pipeline Report

- Timestamp: 2026-11-02T17:47:21.416935Z
- Sources configured: 43
- Raw items: 2258
- Stories: 2199
- Clusters: 2169
- LLM: {'status': 'degraded', 'calls': 155, 'ok': 152, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 56, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 144, 'ok': 141, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 56, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 144}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 155
- Enrichment: 11
- Publish: 144

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.11
- normalize: 0.09
- dedupe: 0.07
- llm_enrich: 17.04
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 683.13
- persist_llm_cache: 0.23