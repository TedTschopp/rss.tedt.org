# Pipeline Report

- Timestamp: 2026-07-15T07:38:16.503426Z
- Sources configured: 43
- Raw items: 1716
- Stories: 1675
- Clusters: 1610
- LLM: {'status': 'ok', 'calls': 933, 'ok': 933, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 180, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 337, 'remaining': 87}, 'summaries': {'before': 292, 'remaining': 42}}}, 'publish': {'status': 'ok', 'calls': 680, 'ok': 680, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 180, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 680}, 'backlog': {'ai_relevance': {'before': 521, 'remaining': 271}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 540, 'remaining': 290}}, 'backlog_remaining': 561}}, 'backlog': {'embeddings': {'before': 337, 'remaining': 87}, 'summaries': {'before': 292, 'remaining': 42}, 'ai_relevance': {'before': 521, 'remaining': 271}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 540, 'remaining': 290}}, 'backlog_remaining': 690}

## LLM Calls
- Total: 933
- Enrichment: 253
- Publish: 680

## Enrichment Backlog
- Remaining: 690
- embeddings: 87
- summaries: 42
- ai_relevance: 271
- importance: 0
- output_cleanup: 290

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.05
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 255.21
- cluster: 0.35
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 716.99
- persist_llm_cache: 0.27