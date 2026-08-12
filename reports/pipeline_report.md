# Pipeline Report

- Timestamp: 2026-08-12T04:52:24.429573Z
- Sources configured: 43
- Raw items: 4064
- Stories: 3208
- Clusters: 3179
- LLM: {'status': 'ok', 'calls': 466, 'ok': 466, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 194, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 440, 'ok': 440, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 194, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 440}, 'backlog': {'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 466
- Enrichment: 26
- Publish: 440

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.17
- normalize: 0.21
- dedupe: 0.11
- llm_enrich: 79.38
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.49
- publish: 2037.06
- persist_llm_cache: 0.23