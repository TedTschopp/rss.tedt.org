# Pipeline Report

- Timestamp: 2026-07-18T01:41:48.484306Z
- Sources configured: 43
- Raw items: 1863
- Stories: 1814
- Clusters: 1782
- LLM: {'status': 'degraded', 'calls': 142, 'ok': 140, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 46, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 131, 'ok': 129, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 46, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 131}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 142
- Enrichment: 11
- Publish: 131

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.70
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 15.08
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 631.95
- persist_llm_cache: 0.20