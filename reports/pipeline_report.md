# Pipeline Report

- Timestamp: 2026-08-02T04:53:57.936474Z
- Sources configured: 43
- Raw items: 1932
- Stories: 1880
- Clusters: 1851
- LLM: {'status': 'degraded', 'calls': 221, 'ok': 220, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 85, 'importance': 63, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'degraded', 'calls': 195, 'ok': 194, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 85, 'importance': 63, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 195}, 'backlog': {'ai_relevance': {'before': 85, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 85, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 221
- Enrichment: 26
- Publish: 195

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.87
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 32.75
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 740.33
- persist_llm_cache: 0.22