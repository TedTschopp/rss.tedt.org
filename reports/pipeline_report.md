# Pipeline Report

- Timestamp: 2026-07-25T16:24:54.152367Z
- Sources configured: 43
- Raw items: 1924
- Stories: 1881
- Clusters: 1851
- LLM: {'status': 'ok', 'calls': 103, 'ok': 103, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 92, 'ok': 92, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 92}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 103
- Enrichment: 11
- Publish: 92

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.86
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 17.29
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 328.90
- persist_llm_cache: 0.20