# Pipeline Report

- Timestamp: 2026-08-07T08:30:45.521305Z
- Sources configured: 43
- Raw items: 1841
- Stories: 1801
- Clusters: 1774
- LLM: {'status': 'ok', 'calls': 83, 'ok': 83, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 20, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 72, 'ok': 72, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 20, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 72}, 'backlog': {'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 83
- Enrichment: 11
- Publish: 72

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.85
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 17.65
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 337.31
- persist_llm_cache: 0.21