# Pipeline Report

- Timestamp: 2026-09-05T08:09:22.108237Z
- Sources configured: 43
- Raw items: 2225
- Stories: 2189
- Clusters: 2158
- LLM: {'status': 'ok', 'calls': 47, 'ok': 47, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 13, 'importance': 3, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 36, 'ok': 36, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 13, 'importance': 3, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 36}, 'backlog': {'ai_relevance': {'before': 13, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 13, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 47
- Enrichment: 11
- Publish: 36

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.96
- normalize: 0.10
- dedupe: 0.06
- llm_enrich: 18.74
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 134.30
- persist_llm_cache: 0.22