# Pipeline Report

- Timestamp: 2026-10-14T00:20:45.324878Z
- Sources configured: 43
- Raw items: 2093
- Stories: 2029
- Clusters: 2002
- LLM: {'status': 'degraded', 'calls': 153, 'ok': 149, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 142, 'ok': 138, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 142}, 'backlog': {'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 153
- Enrichment: 11
- Publish: 142

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.66
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 15.28
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 509.94
- persist_llm_cache: 0.27