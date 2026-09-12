# Pipeline Report

- Timestamp: 2026-09-12T08:17:02.585630Z
- Sources configured: 43
- Raw items: 2429
- Stories: 2122
- Clusters: 2093
- LLM: {'status': 'degraded', 'calls': 182, 'ok': 180, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 75, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}}}, 'publish': {'status': 'degraded', 'calls': 171, 'ok': 169, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 75, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 171}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 182
- Enrichment: 11
- Publish: 171

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 8
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.95
- normalize: 0.11
- dedupe: 0.07
- llm_enrich: 15.63
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 623.57
- persist_llm_cache: 0.21