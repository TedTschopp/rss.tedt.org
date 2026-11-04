# Pipeline Report

- Timestamp: 2026-11-04T11:40:38.647217Z
- Sources configured: 43
- Raw items: 2103
- Stories: 2053
- Clusters: 2025
- LLM: {'status': 'degraded', 'calls': 271, 'ok': 269, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 129, 'importance': 67, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 245, 'ok': 243, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 129, 'importance': 67, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 245}, 'backlog': {'ai_relevance': {'before': 129, 'remaining': 0}, 'importance': {'before': 4, 'remaining': 2}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 129, 'remaining': 0}, 'importance': {'before': 4, 'remaining': 2}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 27}

## LLM Calls
- Total: 271
- Enrichment: 26
- Publish: 245

## Enrichment Backlog
- Remaining: 27
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.67
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 31.80
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 817.66
- persist_llm_cache: 0.27