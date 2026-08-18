# Pipeline Report

- Timestamp: 2026-08-18T16:24:18.882096Z
- Sources configured: 43
- Raw items: 1977
- Stories: 1926
- Clusters: 1896
- LLM: {'status': 'degraded', 'calls': 164, 'ok': 158, 'errors': 6, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 57, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 153, 'ok': 147, 'errors': 6, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 57, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 153}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 6}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 164
- Enrichment: 11
- Publish: 153

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 5
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.48
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 19.74
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 988.20
- persist_llm_cache: 0.22