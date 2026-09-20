# Pipeline Report

- Timestamp: 2026-09-20T16:16:50.217197Z
- Sources configured: 43
- Raw items: 2047
- Stories: 2023
- Clusters: 1995
- LLM: {'status': 'degraded', 'calls': 150, 'ok': 145, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 139, 'ok': 134, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 139}, 'backlog': {'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 5}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 150
- Enrichment: 11
- Publish: 139

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 5
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.90
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 15.17
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 637.04
- persist_llm_cache: 0.19