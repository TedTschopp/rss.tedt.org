# Pipeline Report

- Timestamp: 2026-07-31T16:46:45.159212Z
- Sources configured: 43
- Raw items: 1925
- Stories: 1896
- Clusters: 1867
- LLM: {'status': 'degraded', 'calls': 130, 'ok': 126, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 44, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 119, 'ok': 115, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 44, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 119}, 'backlog': {'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 130
- Enrichment: 11
- Publish: 119

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.67
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 17.72
- cluster: 0.30
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 771.61
- persist_llm_cache: 0.22