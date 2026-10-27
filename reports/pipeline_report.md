# Pipeline Report

- Timestamp: 2026-10-27T00:21:01.049710Z
- Sources configured: 43
- Raw items: 2160
- Stories: 2099
- Clusters: 2072
- LLM: {'status': 'degraded', 'calls': 141, 'ok': 140, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 130, 'ok': 129, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 130}, 'backlog': {'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 141
- Enrichment: 11
- Publish: 130

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 7.89
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 17.29
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 508.22
- persist_llm_cache: 0.22