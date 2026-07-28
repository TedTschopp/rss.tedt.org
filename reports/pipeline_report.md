# Pipeline Report

- Timestamp: 2026-07-28T09:05:54.821034Z
- Sources configured: 43
- Raw items: 1802
- Stories: 1754
- Clusters: 1724
- LLM: {'status': 'degraded', 'calls': 142, 'ok': 139, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 50, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 131, 'ok': 128, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 50, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 131}, 'backlog': {'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 142
- Enrichment: 11
- Publish: 131

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.50
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 16.63
- cluster: 0.20
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 609.13
- persist_llm_cache: 0.16