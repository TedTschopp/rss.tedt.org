# Pipeline Report

- Timestamp: 2026-09-28T16:16:03.986032Z
- Sources configured: 43
- Raw items: 2229
- Stories: 2176
- Clusters: 2148
- LLM: {'status': 'ok', 'calls': 155, 'ok': 155, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 59, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 144, 'ok': 144, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 59, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 144}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 155
- Enrichment: 11
- Publish: 144

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.06
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 19.28
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 528.71
- persist_llm_cache: 0.21