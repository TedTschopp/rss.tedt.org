# Pipeline Report

- Timestamp: 2026-11-15T11:31:39.082474Z
- Sources configured: 43
- Raw items: 2137
- Stories: 2079
- Clusters: 2050
- LLM: {'status': 'ok', 'calls': 155, 'ok': 155, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 32, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'ok', 'calls': 129, 'ok': 129, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 32, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 129}, 'backlog': {'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 47, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 155
- Enrichment: 26
- Publish: 129

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.93
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 31.56
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 392.86
- persist_llm_cache: 0.18