# Pipeline Report

- Timestamp: 2026-09-04T04:04:14.772991Z
- Sources configured: 43
- Raw items: 3265
- Stories: 2450
- Clusters: 2422
- LLM: {'status': 'ok', 'calls': 399, 'ok': 399, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 161, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 373, 'ok': 373, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 161, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 373}, 'backlog': {'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 399
- Enrichment: 26
- Publish: 373

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.00
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 37.76
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 1321.39
- persist_llm_cache: 0.22