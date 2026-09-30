# Pipeline Report

- Timestamp: 2026-09-30T04:03:31.820173Z
- Sources configured: 43
- Raw items: 7623
- Stories: 4660
- Clusters: 4631
- LLM: {'status': 'degraded', 'calls': 387, 'ok': 386, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 160, 'importance': 155, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 23}}}, 'publish': {'status': 'degraded', 'calls': 361, 'ok': 360, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 160, 'importance': 155, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 361}, 'backlog': {'ai_relevance': {'before': 160, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 23}, 'ai_relevance': {'before': 160, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 24}

## LLM Calls
- Total: 387
- Enrichment: 26
- Publish: 361

## Enrichment Backlog
- Remaining: 24
- embeddings: 0
- summaries: 23
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.73
- normalize: 0.51
- dedupe: 0.22
- llm_enrich: 31.73
- cluster: 0.30
- score: 0.04
- write_intermediate_outputs: 0.84
- publish: 949.29
- persist_llm_cache: 0.24