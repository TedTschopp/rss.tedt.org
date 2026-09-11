# Pipeline Report

- Timestamp: 2026-09-11T04:00:37.665782Z
- Sources configured: 43
- Raw items: 3149
- Stories: 2452
- Clusters: 2424
- LLM: {'status': 'ok', 'calls': 380, 'ok': 380, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 159, 'importance': 151, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'ok', 'calls': 354, 'ok': 354, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 159, 'importance': 151, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 354}, 'backlog': {'ai_relevance': {'before': 159, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 159, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 380
- Enrichment: 26
- Publish: 354

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.64
- normalize: 0.16
- dedupe: 0.08
- llm_enrich: 32.56
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 1088.87
- persist_llm_cache: 0.22