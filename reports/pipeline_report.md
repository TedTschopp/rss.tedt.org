# Pipeline Report

- Timestamp: 2026-09-08T16:13:10.053392Z
- Sources configured: 43
- Raw items: 2035
- Stories: 1986
- Clusters: 1956
- LLM: {'status': 'degraded', 'calls': 113, 'ok': 112, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 37, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 102, 'ok': 101, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 37, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 102}, 'backlog': {'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 113
- Enrichment: 11
- Publish: 102

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.69
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 19.63
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.31
- publish: 346.00
- persist_llm_cache: 0.21