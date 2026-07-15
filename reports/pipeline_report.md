# Pipeline Report

- Timestamp: 2026-07-15T06:41:07.020184Z
- Sources configured: 43
- Raw items: 1676
- Stories: 1646
- Clusters: 1599
- LLM: {'status': 'ok', 'calls': 959, 'ok': 959, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 206, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 798, 'remaining': 548}, 'summaries': {'before': 754, 'remaining': 504}}}, 'publish': {'status': 'ok', 'calls': 706, 'ok': 706, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 206, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 706}, 'backlog': {'ai_relevance': {'before': 970, 'remaining': 720}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 1012, 'remaining': 762}}, 'backlog_remaining': 1482}}, 'backlog': {'embeddings': {'before': 798, 'remaining': 548}, 'summaries': {'before': 754, 'remaining': 504}, 'ai_relevance': {'before': 970, 'remaining': 720}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 1012, 'remaining': 762}}, 'backlog_remaining': 2534}

## LLM Calls
- Total: 959
- Enrichment: 253
- Publish: 706

## Enrichment Backlog
- Remaining: 2534
- embeddings: 548
- summaries: 504
- ai_relevance: 720
- importance: 0
- output_cleanup: 762

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.03
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 253.85
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 750.74
- persist_llm_cache: 0.20