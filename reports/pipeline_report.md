# Pipeline Report

- Timestamp: 2026-08-28T06:39:00.354148Z
- Sources configured: 43
- Raw items: 3570
- Stories: 2410
- Clusters: 2382
- LLM: {'status': 'ok', 'calls': 459, 'ok': 459, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 194, 'importance': 189, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 433, 'ok': 433, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 194, 'importance': 189, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 433}, 'backlog': {'ai_relevance': {'before': 194, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 194, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 459
- Enrichment: 26
- Publish: 433

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.33
- normalize: 0.20
- dedupe: 0.10
- llm_enrich: 70.79
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.39
- publish: 1633.32
- persist_llm_cache: 0.22