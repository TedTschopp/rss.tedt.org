# Pipeline Report

- Timestamp: 2026-10-24T08:19:24.060453Z
- Sources configured: 43
- Raw items: 2169
- Stories: 2129
- Clusters: 2100
- LLM: {'status': 'degraded', 'calls': 182, 'ok': 180, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 171, 'ok': 169, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 171}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 182
- Enrichment: 11
- Publish: 171

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 26.49
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 13.95
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.32
- publish: 728.69
- persist_llm_cache: 0.21