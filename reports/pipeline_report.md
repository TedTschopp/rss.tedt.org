# Pipeline Report

- Timestamp: 2026-08-07T04:53:21.306718Z
- Sources configured: 43
- Raw items: 3429
- Stories: 2367
- Clusters: 2340
- LLM: {'status': 'ok', 'calls': 463, 'ok': 463, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 192, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 437, 'ok': 437, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 192, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 437}, 'backlog': {'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 463
- Enrichment: 26
- Publish: 437

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.47
- normalize: 0.21
- dedupe: 0.10
- llm_enrich: 71.63
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.40
- publish: 1868.21
- persist_llm_cache: 0.23