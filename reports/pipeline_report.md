# Pipeline Report

- Timestamp: 2026-10-12T04:17:51.117017Z
- Sources configured: 43
- Raw items: 3986
- Stories: 2729
- Clusters: 2701
- LLM: {'status': 'ok', 'calls': 472, 'ok': 472, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 198, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 446, 'ok': 446, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 198, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 446}, 'backlog': {'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 472
- Enrichment: 26
- Publish: 446

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 15.28
- normalize: 0.22
- dedupe: 0.10
- llm_enrich: 47.80
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.44
- publish: 990.36
- persist_llm_cache: 0.24