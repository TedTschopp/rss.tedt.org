# Pipeline Report

- Timestamp: 2026-10-17T03:53:06.446233Z
- Sources configured: 43
- Raw items: 2000
- Stories: 1951
- Clusters: 1923
- LLM: {'status': 'degraded', 'calls': 191, 'ok': 190, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 42, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}}}, 'publish': {'status': 'degraded', 'calls': 165, 'ok': 164, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 42, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 165}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 23}

## LLM Calls
- Total: 191
- Enrichment: 26
- Publish: 165

## Enrichment Backlog
- Remaining: 23
- embeddings: 0
- summaries: 22
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 25.56
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 29.49
- cluster: 0.22
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 552.86
- persist_llm_cache: 0.24