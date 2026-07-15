# Pipeline Report

- Timestamp: 2026-07-15T08:33:42.221945Z
- Sources configured: 43
- Raw items: 1571
- Stories: 1541
- Clusters: 1477
- LLM: {'status': 'degraded', 'calls': 121, 'ok': 120, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 26, 'importance': 17, 'output_cleanup': 43}, 'stages': {'enrichment': {'status': 'ok', 'calls': 35, 'ok': 35, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 34, 'remaining': 0}}}, 'publish': {'status': 'degraded', 'calls': 86, 'ok': 85, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 26, 'importance': 17, 'output_cleanup': 43}, 'by_model': {'openai/gpt-4.1-mini': 86}, 'backlog': {'ai_relevance': {'before': 41, 'remaining': 15}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 58, 'remaining': 15}}, 'backlog_remaining': 31}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 34, 'remaining': 0}, 'ai_relevance': {'before': 41, 'remaining': 15}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 58, 'remaining': 15}}, 'backlog_remaining': 31}

## LLM Calls
- Total: 121
- Enrichment: 35
- Publish: 86

## Enrichment Backlog
- Remaining: 31
- embeddings: 0
- summaries: 0
- ai_relevance: 15
- importance: 1
- output_cleanup: 15

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.41
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 44.15
- cluster: 0.29
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 199.21
- persist_llm_cache: 0.24