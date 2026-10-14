# Pipeline Report

- Timestamp: 2026-10-14T08:13:25.593859Z
- Sources configured: 43
- Raw items: 7452
- Stories: 4573
- Clusters: 4546
- LLM: {'status': 'ok', 'calls': 184, 'ok': 184, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 173, 'ok': 173, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 173}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 184
- Enrichment: 11
- Publish: 173

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.56
- normalize: 0.48
- dedupe: 0.21
- llm_enrich: 14.75
- cluster: 0.30
- score: 0.04
- write_intermediate_outputs: 0.81
- publish: 372.05
- persist_llm_cache: 0.23