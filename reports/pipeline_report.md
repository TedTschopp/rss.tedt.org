# Pipeline Report

- Timestamp: 2026-09-14T08:19:05.691529Z
- Sources configured: 43
- Raw items: 3073
- Stories: 2385
- Clusters: 2352
- LLM: {'status': 'degraded', 'calls': 187, 'ok': 186, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 176, 'ok': 175, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 176}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 187
- Enrichment: 11
- Publish: 176

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.74
- normalize: 0.16
- dedupe: 0.08
- llm_enrich: 18.18
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.36
- publish: 648.89
- persist_llm_cache: 0.22