# Pipeline Report

- Timestamp: 2026-11-17T07:11:48.483506Z
- Sources configured: 43
- Raw items: 2326
- Stories: 2267
- Clusters: 2238
- LLM: {'status': 'degraded', 'calls': 190, 'ok': 189, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 79, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 179, 'ok': 178, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 79, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 179}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 190
- Enrichment: 11
- Publish: 179

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.35
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 13.87
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 729.60
- persist_llm_cache: 0.21