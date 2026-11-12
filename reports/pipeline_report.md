# Pipeline Report

- Timestamp: 2026-11-12T06:15:47.368553Z
- Sources configured: 43
- Raw items: 2211
- Stories: 2161
- Clusters: 2131
- LLM: {'status': 'ok', 'calls': 97, 'ok': 97, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 36, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 86, 'ok': 86, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 36, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 86}, 'backlog': {'ai_relevance': {'before': 36, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 36, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 97
- Enrichment: 11
- Publish: 86

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.14
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 15.47
- cluster: 0.16
- score: 0.02
- write_intermediate_outputs: 0.20
- publish: 286.17
- persist_llm_cache: 0.24