# Pipeline Report

- Timestamp: 2026-08-18T04:13:00.463007Z
- Sources configured: 43
- Raw items: 2908
- Stories: 2280
- Clusters: 2248
- LLM: {'status': 'ok', 'calls': 408, 'ok': 408, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 172, 'importance': 166, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 382, 'ok': 382, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 172, 'importance': 166, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 382}, 'backlog': {'ai_relevance': {'before': 172, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 172, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 408
- Enrichment: 26
- Publish: 382

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.67
- normalize: 0.14
- dedupe: 0.08
- llm_enrich: 34.84
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.34
- publish: 1420.78
- persist_llm_cache: 0.23