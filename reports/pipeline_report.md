# Pipeline Report

- Timestamp: 2026-10-25T16:13:04.259194Z
- Sources configured: 43
- Raw items: 2153
- Stories: 2099
- Clusters: 2071
- LLM: {'status': 'degraded', 'calls': 113, 'ok': 111, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 102, 'ok': 100, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 102}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 113
- Enrichment: 11
- Publish: 102

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.88
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.36
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 439.81
- persist_llm_cache: 0.22