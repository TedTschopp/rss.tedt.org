# Pipeline Report

- Timestamp: 2026-07-15T09:00:40.876663Z
- Sources configured: 43
- Raw items: 1553
- Stories: 1518
- Clusters: 1453
- LLM: {'status': 'degraded', 'calls': 172, 'ok': 171, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 35, 'output_cleanup': 53}, 'stages': {'enrichment': {'status': 'ok', 'calls': 40, 'ok': 40, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 39, 'remaining': 0}}}, 'publish': {'status': 'degraded', 'calls': 132, 'ok': 131, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 35, 'output_cleanup': 53}, 'by_model': {'openai/gpt-4.1-mini': 132}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 15}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 68, 'remaining': 15}}, 'backlog_remaining': 31}}, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 39, 'remaining': 0}, 'ai_relevance': {'before': 59, 'remaining': 15}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 68, 'remaining': 15}}, 'backlog_remaining': 31}

## LLM Calls
- Total: 172
- Enrichment: 40
- Publish: 132

## Enrichment Backlog
- Remaining: 31
- embeddings: 0
- summaries: 0
- ai_relevance: 15
- importance: 1
- output_cleanup: 15

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.80
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 41.83
- cluster: 0.33
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 204.28
- persist_llm_cache: 0.25