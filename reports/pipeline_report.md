# Pipeline Report

- Timestamp: 2026-08-08T16:16:20.175403Z
- Sources configured: 43
- Raw items: 2019
- Stories: 1969
- Clusters: 1941
- LLM: {'status': 'ok', 'calls': 109, 'ok': 109, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 98, 'ok': 98, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 98}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 109
- Enrichment: 11
- Publish: 98

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.49
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 19.76
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.27
- publish: 443.03
- persist_llm_cache: 0.13