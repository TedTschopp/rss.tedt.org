# Pipeline Report

- Timestamp: 2026-11-26T13:22:10.624688Z
- Sources configured: 43
- Raw items: 2125
- Stories: 2095
- Clusters: 2062
- LLM: {'status': 'degraded', 'calls': 291, 'ok': 290, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 119, 'importance': 96, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 265, 'ok': 264, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 119, 'importance': 96, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 265}, 'backlog': {'ai_relevance': {'before': 119, 'remaining': 1}, 'importance': {'before': 2, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 119, 'remaining': 1}, 'importance': {'before': 2, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 291
- Enrichment: 26
- Publish: 265

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 21
- ai_relevance: 1
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 4.88
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 36.03
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 1182.49
- persist_llm_cache: 0.30