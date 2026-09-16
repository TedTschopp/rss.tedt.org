# Pipeline Report

- Timestamp: 2026-09-16T08:14:27.762450Z
- Sources configured: 43
- Raw items: 3871
- Stories: 3093
- Clusters: 3060
- LLM: {'status': 'ok', 'calls': 181, 'ok': 181, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 170, 'ok': 170, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 170}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 181
- Enrichment: 11
- Publish: 170

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.42
- normalize: 0.22
- dedupe: 0.11
- llm_enrich: 17.31
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.46
- publish: 385.44
- persist_llm_cache: 0.22