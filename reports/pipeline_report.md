# Pipeline Report

- Timestamp: 2026-08-09T04:12:33.891775Z
- Sources configured: 43
- Raw items: 1840
- Stories: 1799
- Clusters: 1772
- LLM: {'status': 'ok', 'calls': 153, 'ok': 153, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 29, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'ok', 'calls': 127, 'ok': 127, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 29, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 127}, 'backlog': {'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 153
- Enrichment: 26
- Publish: 127

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.88
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 38.00
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 504.23
- persist_llm_cache: 0.19