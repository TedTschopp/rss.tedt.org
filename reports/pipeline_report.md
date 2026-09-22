# Pipeline Report

- Timestamp: 2026-09-22T00:17:56.305338Z
- Sources configured: 43
- Raw items: 2060
- Stories: 2008
- Clusters: 1980
- LLM: {'status': 'ok', 'calls': 142, 'ok': 142, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 47, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 131, 'ok': 131, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 47, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 131}, 'backlog': {'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 142
- Enrichment: 11
- Publish: 131

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.57
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 13.43
- cluster: 0.18
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 299.25
- persist_llm_cache: 0.17