# Pipeline Report

- Timestamp: 2026-07-22T17:22:07.870633Z
- Sources configured: 43
- Raw items: 1944
- Stories: 1887
- Clusters: 1859
- LLM: {'status': 'degraded', 'calls': 164, 'ok': 162, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 60, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 153, 'ok': 151, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 60, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 153}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 164
- Enrichment: 11
- Publish: 153

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.37
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 21.09
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 764.78
- persist_llm_cache: 0.21