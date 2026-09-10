# Pipeline Report

- Timestamp: 2026-09-10T04:03:11.613298Z
- Sources configured: 43
- Raw items: 5627
- Stories: 3492
- Clusters: 3462
- LLM: {'status': 'ok', 'calls': 407, 'ok': 407, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 167, 'importance': 166, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 24}}}, 'publish': {'status': 'ok', 'calls': 381, 'ok': 381, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 167, 'importance': 166, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 381}, 'backlog': {'ai_relevance': {'before': 167, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 24}, 'ai_relevance': {'before': 167, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 24}

## LLM Calls
- Total: 407
- Enrichment: 26
- Publish: 381

## Enrichment Backlog
- Remaining: 24
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.95
- normalize: 0.35
- dedupe: 0.16
- llm_enrich: 36.28
- cluster: 0.28
- score: 0.04
- write_intermediate_outputs: 0.62
- publish: 1251.48
- persist_llm_cache: 0.23