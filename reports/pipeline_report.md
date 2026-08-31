# Pipeline Report

- Timestamp: 2026-08-31T16:18:30.085554Z
- Sources configured: 43
- Raw items: 2019
- Stories: 1964
- Clusters: 1936
- LLM: {'status': 'degraded', 'calls': 151, 'ok': 147, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 51, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 140, 'ok': 136, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 51, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 140}, 'backlog': {'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 151
- Enrichment: 11
- Publish: 140

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
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 21.27
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 705.41
- persist_llm_cache: 0.20