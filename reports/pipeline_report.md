# Pipeline Report

- Timestamp: 2026-07-23T06:51:50.441923Z
- Sources configured: 43
- Raw items: 3263
- Stories: 2588
- Clusters: 2559
- LLM: {'status': 'ok', 'calls': 465, 'ok': 465, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 193, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 439, 'ok': 439, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 193, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 439}, 'backlog': {'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 465
- Enrichment: 26
- Publish: 439

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.54
- normalize: 0.15
- dedupe: 0.08
- llm_enrich: 50.65
- cluster: 0.24
- score: 0.03
- write_intermediate_outputs: 0.39
- publish: 1988.39
- persist_llm_cache: 0.23