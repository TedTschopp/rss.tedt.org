# Pipeline Report

- Timestamp: 2026-10-05T16:15:04.369179Z
- Sources configured: 43
- Raw items: 2114
- Stories: 2060
- Clusters: 2033
- LLM: {'status': 'degraded', 'calls': 168, 'ok': 166, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 60, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 157, 'ok': 155, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 60, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 157}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 168
- Enrichment: 11
- Publish: 157

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.77
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 15.25
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 479.37
- persist_llm_cache: 0.22