# Pipeline Report

- Timestamp: 2026-09-11T08:16:44.309982Z
- Sources configured: 43
- Raw items: 3360
- Stories: 2640
- Clusters: 2612
- LLM: {'status': 'ok', 'calls': 171, 'ok': 171, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 71, 'importance': 69, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 160, 'ok': 160, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 71, 'importance': 69, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 160}, 'backlog': {'ai_relevance': {'before': 71, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 71, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 171
- Enrichment: 11
- Publish: 160

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.78
- normalize: 0.12
- dedupe: 0.06
- llm_enrich: 14.94
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.38
- publish: 523.14
- persist_llm_cache: 0.15