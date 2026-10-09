# Pipeline Report

- Timestamp: 2026-10-09T04:05:58.136772Z
- Sources configured: 43
- Raw items: 4106
- Stories: 2899
- Clusters: 2870
- LLM: {'status': 'ok', 'calls': 405, 'ok': 405, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 167, 'importance': 167, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'ok', 'calls': 379, 'ok': 379, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 167, 'importance': 167, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 379}, 'backlog': {'ai_relevance': {'before': 167, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 167, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 405
- Enrichment: 26
- Publish: 379

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.36
- normalize: 0.12
- dedupe: 0.06
- llm_enrich: 30.77
- cluster: 0.18
- score: 0.02
- write_intermediate_outputs: 0.32
- publish: 932.92
- persist_llm_cache: 0.20