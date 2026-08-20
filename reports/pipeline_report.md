# Pipeline Report

- Timestamp: 2026-08-20T00:17:11.134815Z
- Sources configured: 43
- Raw items: 2005
- Stories: 1948
- Clusters: 1919
- LLM: {'status': 'ok', 'calls': 142, 'ok': 142, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 131, 'ok': 131, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 131}, 'backlog': {'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 142
- Enrichment: 11
- Publish: 131

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.64
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 14.77
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 494.24
- persist_llm_cache: 0.21