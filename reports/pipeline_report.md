# Pipeline Report

- Timestamp: 2026-10-31T03:44:39.626647Z
- Sources configured: 43
- Raw items: 2108
- Stories: 2055
- Clusters: 2028
- LLM: {'status': 'degraded', 'calls': 133, 'ok': 132, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 25, 'output_cleanup': 42}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 107, 'ok': 106, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 25, 'output_cleanup': 42}, 'by_model': {'openai/gpt-4.1-mini': 107}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 133
- Enrichment: 26
- Publish: 107

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.18
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 30.17
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 457.33
- persist_llm_cache: 0.24