# Pipeline Report

- Timestamp: 2026-09-11T00:19:11.597856Z
- Sources configured: 43
- Raw items: 2023
- Stories: 1962
- Clusters: 1934
- LLM: {'status': 'ok', 'calls': 143, 'ok': 143, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 49, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 132, 'ok': 132, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 49, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 132}, 'backlog': {'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 143
- Enrichment: 11
- Publish: 132

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.14
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 17.78
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 386.27
- persist_llm_cache: 0.22