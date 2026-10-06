# Pipeline Report

- Timestamp: 2026-10-06T16:15:18.515399Z
- Sources configured: 43
- Raw items: 2141
- Stories: 2092
- Clusters: 2061
- LLM: {'status': 'degraded', 'calls': 157, 'ok': 155, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 54, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 146, 'ok': 144, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 54, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 146}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 157
- Enrichment: 11
- Publish: 146

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.30
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 17.74
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 491.88
- persist_llm_cache: 0.22