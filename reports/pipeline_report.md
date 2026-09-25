# Pipeline Report

- Timestamp: 2026-09-25T19:30:43.479050Z
- Sources configured: 43
- Raw items: 4041
- Stories: 2750
- Clusters: 2723
- LLM: {'status': 'degraded', 'calls': 468, 'ok': 467, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 200, 'importance': 192, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 442, 'ok': 441, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 200, 'importance': 192, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 442}, 'backlog': {'ai_relevance': {'before': 200, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 200, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 26}

## LLM Calls
- Total: 468
- Enrichment: 26
- Publish: 442

## Enrichment Backlog
- Remaining: 26
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.73
- normalize: 0.23
- dedupe: 0.11
- llm_enrich: 32.46
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.45
- publish: 1246.08
- persist_llm_cache: 0.22