# Pipeline Report

- Timestamp: 2026-10-04T05:16:59.924492Z
- Sources configured: 43
- Raw items: 1971
- Stories: 1931
- Clusters: 1904
- LLM: {'status': 'degraded', 'calls': 172, 'ok': 171, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 25, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 146, 'ok': 145, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 25, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 146}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 172
- Enrichment: 26
- Publish: 146

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.17
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 28.89
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 361.28
- persist_llm_cache: 0.22