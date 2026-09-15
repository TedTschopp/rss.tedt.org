# Pipeline Report

- Timestamp: 2026-09-15T04:02:24.303281Z
- Sources configured: 43
- Raw items: 3158
- Stories: 2463
- Clusters: 2433
- LLM: {'status': 'ok', 'calls': 397, 'ok': 397, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 160, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'ok', 'calls': 371, 'ok': 371, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 160, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 371}, 'backlog': {'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 397
- Enrichment: 26
- Publish: 371

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.29
- normalize: 0.11
- dedupe: 0.07
- llm_enrich: 45.16
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 1161.12
- persist_llm_cache: 0.18