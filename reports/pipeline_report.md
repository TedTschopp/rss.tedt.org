# Pipeline Report

- Timestamp: 2026-11-08T10:51:06.559635Z
- Sources configured: 43
- Raw items: 2081
- Stories: 2040
- Clusters: 2012
- LLM: {'status': 'degraded', 'calls': 159, 'ok': 158, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 30, 'ai_relevance': 55, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 133, 'ok': 132, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 30, 'ai_relevance': 55, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 133}, 'backlog': {'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 159
- Enrichment: 26
- Publish: 133

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.16
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 27.98
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 488.77
- persist_llm_cache: 0.29