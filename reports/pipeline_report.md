# Pipeline Report

- Timestamp: 2026-08-31T03:53:52.105971Z
- Sources configured: 43
- Raw items: 1912
- Stories: 1860
- Clusters: 1833
- LLM: {'status': 'degraded', 'calls': 156, 'ok': 155, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 30, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}}}, 'publish': {'status': 'degraded', 'calls': 130, 'ok': 129, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 30, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 130}, 'backlog': {'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}, 'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 156
- Enrichment: 26
- Publish: 130

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 18
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.98
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 33.15
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 631.49
- persist_llm_cache: 0.21