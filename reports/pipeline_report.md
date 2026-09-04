# Pipeline Report

- Timestamp: 2026-09-04T08:21:06.250735Z
- Sources configured: 43
- Raw items: 3513
- Stories: 2469
- Clusters: 2441
- LLM: {'status': 'ok', 'calls': 181, 'ok': 181, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 170, 'ok': 170, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 170}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 181
- Enrichment: 11
- Publish: 170

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.67
- normalize: 0.10
- dedupe: 0.06
- llm_enrich: 20.21
- cluster: 0.18
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 792.21
- persist_llm_cache: 0.13