# Pipeline Report

- Timestamp: 2026-09-09T03:47:32.739660Z
- Sources configured: 43
- Raw items: 1957
- Stories: 1911
- Clusters: 1881
- LLM: {'status': 'degraded', 'calls': 129, 'ok': 128, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 29, 'importance': 27, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'degraded', 'calls': 103, 'ok': 102, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 29, 'importance': 27, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 103}, 'backlog': {'ai_relevance': {'before': 29, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 29, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 129
- Enrichment: 26
- Publish: 103

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.79
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 32.28
- cluster: 0.22
- score: 0.01
- write_intermediate_outputs: 0.21
- publish: 320.16
- persist_llm_cache: 0.17