# Pipeline Report

- Timestamp: 2026-07-30T16:42:23.733471Z
- Sources configured: 43
- Raw items: 1901
- Stories: 1864
- Clusters: 1835
- LLM: {'status': 'degraded', 'calls': 160, 'ok': 159, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 60, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 149, 'ok': 148, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 60, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 149}, 'backlog': {'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 160
- Enrichment: 11
- Publish: 149

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.08
- normalize: 0.06
- dedupe: 0.06
- llm_enrich: 17.06
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 627.54
- persist_llm_cache: 0.22