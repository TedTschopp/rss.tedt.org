# Pipeline Report

- Timestamp: 2026-08-06T09:02:08.686756Z
- Sources configured: 43
- Raw items: 1916
- Stories: 1869
- Clusters: 1842
- LLM: {'status': 'ok', 'calls': 99, 'ok': 99, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 38, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 88, 'ok': 88, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 38, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 88}, 'backlog': {'ai_relevance': {'before': 38, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 38, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 99
- Enrichment: 11
- Publish: 88

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.69
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 15.39
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 348.67
- persist_llm_cache: 0.22