# Pipeline Report

- Timestamp: 2026-11-11T11:40:58.228686Z
- Sources configured: 43
- Raw items: 2145
- Stories: 2093
- Clusters: 2065
- LLM: {'status': 'degraded', 'calls': 300, 'ok': 299, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 97, 'ai_relevance': 127, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'degraded', 'calls': 274, 'ok': 273, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 97, 'ai_relevance': 127, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 274}, 'backlog': {'ai_relevance': {'before': 127, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 127, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 300
- Enrichment: 26
- Publish: 274

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.11
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 46.49
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 1050.47
- persist_llm_cache: 0.30