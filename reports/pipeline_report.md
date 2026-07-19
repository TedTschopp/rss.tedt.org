# Pipeline Report

- Timestamp: 2026-07-19T06:31:15.192800Z
- Sources configured: 43
- Raw items: 1872
- Stories: 1826
- Clusters: 1797
- LLM: {'status': 'degraded', 'calls': 268, 'ok': 267, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 129, 'importance': 63, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'degraded', 'calls': 242, 'ok': 241, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 129, 'importance': 63, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 242}, 'backlog': {'ai_relevance': {'before': 129, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 129, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 268
- Enrichment: 26
- Publish: 242

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.56
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 36.60
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 972.92
- persist_llm_cache: 0.25