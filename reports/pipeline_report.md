# Pipeline Report

- Timestamp: 2026-08-27T05:46:26.771084Z
- Sources configured: 43
- Raw items: 3717
- Stories: 2799
- Clusters: 2771
- LLM: {'status': 'ok', 'calls': 416, 'ok': 416, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 181, 'importance': 159, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 390, 'ok': 390, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 181, 'importance': 159, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 390}, 'backlog': {'ai_relevance': {'before': 181, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 181, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 416
- Enrichment: 26
- Publish: 390

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.97
- normalize: 0.19
- dedupe: 0.10
- llm_enrich: 64.22
- cluster: 0.30
- score: 0.03
- write_intermediate_outputs: 0.44
- publish: 1480.35
- persist_llm_cache: 0.24