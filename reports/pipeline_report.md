# Pipeline Report

- Timestamp: 2026-09-15T16:16:01.676395Z
- Sources configured: 43
- Raw items: 2051
- Stories: 1996
- Clusters: 1964
- LLM: {'status': 'degraded', 'calls': 172, 'ok': 169, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 64, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 161, 'ok': 158, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 64, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 161}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 172
- Enrichment: 11
- Publish: 161

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.03
- ingestion: 2.27
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 15.75
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 566.11
- persist_llm_cache: 0.21