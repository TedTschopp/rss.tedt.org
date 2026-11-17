# Pipeline Report

- Timestamp: 2026-11-17T17:39:10.082599Z
- Sources configured: 43
- Raw items: 2274
- Stories: 2215
- Clusters: 2187
- LLM: {'status': 'degraded', 'calls': 174, 'ok': 171, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 68, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 163, 'ok': 160, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 68, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 163}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 75, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 174
- Enrichment: 11
- Publish: 163

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.88
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 18.26
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 587.92
- persist_llm_cache: 0.28