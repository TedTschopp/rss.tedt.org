# Pipeline Report

- Timestamp: 2026-11-23T06:26:46.371127Z
- Sources configured: 43
- Raw items: 3999
- Stories: 2822
- Clusters: 2793
- LLM: {'status': 'degraded', 'calls': 185, 'ok': 183, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}}}, 'publish': {'status': 'degraded', 'calls': 174, 'ok': 172, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 174}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 185
- Enrichment: 11
- Publish: 174

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 11
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.12
- normalize: 0.15
- dedupe: 0.08
- llm_enrich: 16.33
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.44
- publish: 674.22
- persist_llm_cache: 0.28