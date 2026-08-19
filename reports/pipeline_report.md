# Pipeline Report

- Timestamp: 2026-08-19T04:14:48.521366Z
- Sources configured: 43
- Raw items: 4469
- Stories: 2976
- Clusters: 2946
- LLM: {'status': 'ok', 'calls': 425, 'ok': 425, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 178, 'importance': 176, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}}}, 'publish': {'status': 'ok', 'calls': 399, 'ok': 399, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 178, 'importance': 176, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 399}, 'backlog': {'ai_relevance': {'before': 178, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}, 'ai_relevance': {'before': 178, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 425
- Enrichment: 26
- Publish: 399

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 22
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.66
- normalize: 0.25
- dedupe: 0.12
- llm_enrich: 33.01
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.51
- publish: 1500.22
- persist_llm_cache: 0.22