# Pipeline Report

- Timestamp: 2026-11-15T20:59:31.182319Z
- Sources configured: 43
- Raw items: 2120
- Stories: 2071
- Clusters: 2043
- LLM: {'status': 'degraded', 'calls': 88, 'ok': 86, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 24, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 77, 'ok': 75, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 24, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 77}, 'backlog': {'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 88
- Enrichment: 11
- Publish: 77

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.19
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 14.35
- cluster: 0.16
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 331.81
- persist_llm_cache: 0.21