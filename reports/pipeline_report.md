# Pipeline Report

- Timestamp: 2026-10-05T04:00:37.160194Z
- Sources configured: 43
- Raw items: 2052
- Stories: 2010
- Clusters: 1982
- LLM: {'status': 'degraded', 'calls': 149, 'ok': 148, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 27, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 123, 'ok': 122, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 27, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 123}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 149
- Enrichment: 26
- Publish: 123

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.44
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 30.95
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 410.70
- persist_llm_cache: 0.25