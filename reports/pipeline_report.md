# Pipeline Report

- Timestamp: 2026-10-26T03:57:09.264394Z
- Sources configured: 43
- Raw items: 2111
- Stories: 2069
- Clusters: 2041
- LLM: {'status': 'degraded', 'calls': 132, 'ok': 131, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 27, 'output_cleanup': 42}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'degraded', 'calls': 106, 'ok': 105, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 27, 'output_cleanup': 42}, 'by_model': {'openai/gpt-4.1-mini': 106}, 'backlog': {'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 132
- Enrichment: 26
- Publish: 106

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.61
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 28.50
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 407.31
- persist_llm_cache: 0.21