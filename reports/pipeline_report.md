# Pipeline Report

- Timestamp: 2026-08-05T09:01:39.309799Z
- Sources configured: 43
- Raw items: 1890
- Stories: 1843
- Clusters: 1816
- LLM: {'status': 'degraded', 'calls': 88, 'ok': 87, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 35, 'importance': 22, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 77, 'ok': 76, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 35, 'importance': 22, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 77}, 'backlog': {'ai_relevance': {'before': 35, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 35, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 88
- Enrichment: 11
- Publish: 77

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.88
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 19.40
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 323.58
- persist_llm_cache: 0.21