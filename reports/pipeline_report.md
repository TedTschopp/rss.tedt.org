# Pipeline Report

- Timestamp: 2026-08-20T08:24:58.999407Z
- Sources configured: 43
- Raw items: 3315
- Stories: 2593
- Clusters: 2563
- LLM: {'status': 'ok', 'calls': 180, 'ok': 180, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 169, 'ok': 169, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 169}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 180
- Enrichment: 11
- Publish: 169

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.44
- normalize: 0.16
- dedupe: 0.08
- llm_enrich: 19.92
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.43
- publish: 750.41
- persist_llm_cache: 0.21