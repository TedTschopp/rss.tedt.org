# Pipeline Report

- Timestamp: 2026-10-24T16:13:12.593778Z
- Sources configured: 43
- Raw items: 2186
- Stories: 2133
- Clusters: 2103
- LLM: {'status': 'degraded', 'calls': 143, 'ok': 141, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 51, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 132, 'ok': 130, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 51, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 132}, 'backlog': {'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 143
- Enrichment: 11
- Publish: 132

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 4.06
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 13.76
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 441.55
- persist_llm_cache: 0.22