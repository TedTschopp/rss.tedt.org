# Pipeline Report

- Timestamp: 2026-08-08T04:10:22.832111Z
- Sources configured: 43
- Raw items: 1912
- Stories: 1864
- Clusters: 1836
- LLM: {'status': 'ok', 'calls': 187, 'ok': 187, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 84, 'importance': 33, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 161, 'ok': 161, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 84, 'importance': 33, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 161}, 'backlog': {'ai_relevance': {'before': 84, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 84, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 187
- Enrichment: 26
- Publish: 161

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 25.73
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 36.37
- cluster: 0.19
- score: 0.01
- write_intermediate_outputs: 0.24
- publish: 636.05
- persist_llm_cache: 0.17