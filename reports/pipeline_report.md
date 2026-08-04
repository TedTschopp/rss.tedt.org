# Pipeline Report

- Timestamp: 2026-08-04T05:11:05.397479Z
- Sources configured: 43
- Raw items: 5021
- Stories: 3396
- Clusters: 3368
- LLM: {'status': 'degraded', 'calls': 469, 'ok': 468, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 197, 'importance': 196, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 443, 'ok': 442, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 197, 'importance': 196, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 443}, 'backlog': {'ai_relevance': {'before': 197, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 197, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 26}

## LLM Calls
- Total: 469
- Enrichment: 26
- Publish: 443

## Enrichment Backlog
- Remaining: 26
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.35
- normalize: 0.27
- dedupe: 0.13
- llm_enrich: 62.26
- cluster: 0.25
- score: 0.04
- write_intermediate_outputs: 0.62
- publish: 1968.14
- persist_llm_cache: 0.23