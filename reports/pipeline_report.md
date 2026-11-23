# Pipeline Report

- Timestamp: 2026-11-23T13:47:53.545373Z
- Sources configured: 43
- Raw items: 2287
- Stories: 2235
- Clusters: 2204
- LLM: {'status': 'ok', 'calls': 244, 'ok': 244, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 98, 'importance': 70, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 218, 'ok': 218, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 98, 'importance': 70, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 218}, 'backlog': {'ai_relevance': {'before': 98, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 98, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 244
- Enrichment: 26
- Publish: 218

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 4.02
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 39.49
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 915.88
- persist_llm_cache: 0.18