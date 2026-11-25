# Pipeline Report

- Timestamp: 2026-11-25T18:39:37.643590Z
- Sources configured: 43
- Raw items: 2366
- Stories: 2337
- Clusters: 2307
- LLM: {'status': 'degraded', 'calls': 127, 'ok': 126, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 46, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 116, 'ok': 115, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 46, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 116}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 127
- Enrichment: 11
- Publish: 116

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.86
- normalize: 0.09
- dedupe: 0.07
- llm_enrich: 15.35
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.30
- publish: 482.05
- persist_llm_cache: 0.28