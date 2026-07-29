# Pipeline Report

- Timestamp: 2026-07-29T05:56:47.597814Z
- Sources configured: 43
- Raw items: 3419
- Stories: 2336
- Clusters: 2309
- LLM: {'status': 'degraded', 'calls': 468, 'ok': 459, 'errors': 9, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 194, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 442, 'ok': 433, 'errors': 9, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 194, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 442}, 'backlog': {'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 9}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 9}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 9}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 34}

## LLM Calls
- Total: 468
- Enrichment: 26
- Publish: 442

## Enrichment Backlog
- Remaining: 34
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 9
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.40
- normalize: 0.18
- dedupe: 0.10
- llm_enrich: 60.23
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.40
- publish: 4648.04
- persist_llm_cache: 0.25