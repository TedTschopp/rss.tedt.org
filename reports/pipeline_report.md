# Pipeline Report

- Timestamp: 2026-07-22T06:46:49.538605Z
- Sources configured: 43
- Raw items: 3419
- Stories: 2311
- Clusters: 2283
- LLM: {'status': 'ok', 'calls': 459, 'ok': 459, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 192, 'importance': 191, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 433, 'ok': 433, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 192, 'importance': 191, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 433}, 'backlog': {'ai_relevance': {'before': 192, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 192, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 459
- Enrichment: 26
- Publish: 433

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.95
- normalize: 0.15
- dedupe: 0.07
- llm_enrich: 58.54
- cluster: 0.20
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 2012.16
- persist_llm_cache: 0.29