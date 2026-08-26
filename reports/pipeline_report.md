# Pipeline Report

- Timestamp: 2026-08-26T04:25:29.391454Z
- Sources configured: 43
- Raw items: 4445
- Stories: 2998
- Clusters: 2969
- LLM: {'status': 'ok', 'calls': 432, 'ok': 432, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 182, 'importance': 179, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 40, 'remaining': 15}}}, 'publish': {'status': 'ok', 'calls': 406, 'ok': 406, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 182, 'importance': 179, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 406}, 'backlog': {'ai_relevance': {'before': 182, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 40, 'remaining': 15}, 'ai_relevance': {'before': 182, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 15}

## LLM Calls
- Total: 432
- Enrichment: 26
- Publish: 406

## Enrichment Backlog
- Remaining: 15
- embeddings: 0
- summaries: 15
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.39
- normalize: 0.29
- dedupe: 0.13
- llm_enrich: 42.89
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.50
- publish: 2066.18
- persist_llm_cache: 0.23