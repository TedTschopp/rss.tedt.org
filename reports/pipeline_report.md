# Pipeline Report

- Timestamp: 2026-11-17T12:55:20.196131Z
- Sources configured: 43
- Raw items: 5401
- Stories: 3507
- Clusters: 3479
- LLM: {'status': 'degraded', 'calls': 470, 'ok': 469, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 195, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'degraded', 'calls': 444, 'ok': 443, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 195, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 444}, 'backlog': {'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 470
- Enrichment: 26
- Publish: 444

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.55
- normalize: 0.29
- dedupe: 0.15
- llm_enrich: 38.52
- cluster: 0.26
- score: 0.04
- write_intermediate_outputs: 0.63
- publish: 2092.95
- persist_llm_cache: 0.29