# Pipeline Report

- Timestamp: 2026-07-26T16:28:32.284158Z
- Sources configured: 43
- Raw items: 1904
- Stories: 1858
- Clusters: 1830
- LLM: {'status': 'ok', 'calls': 111, 'ok': 111, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 35, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 100, 'ok': 100, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 35, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 100}, 'backlog': {'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 111
- Enrichment: 11
- Publish: 100

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.35
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 16.41
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 453.39
- persist_llm_cache: 0.21