# Pipeline Report

- Timestamp: 2026-08-18T00:14:00.872497Z
- Sources configured: 43
- Raw items: 1962
- Stories: 1914
- Clusters: 1883
- LLM: {'status': 'ok', 'calls': 123, 'ok': 123, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 112, 'ok': 112, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 112}, 'backlog': {'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 123
- Enrichment: 11
- Publish: 112

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.24
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 16.10
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.30
- publish: 347.82
- persist_llm_cache: 0.17