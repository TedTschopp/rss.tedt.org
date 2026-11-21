# Pipeline Report

- Timestamp: 2026-11-21T21:37:44.776702Z
- Sources configured: 43
- Raw items: 2169
- Stories: 2139
- Clusters: 2110
- LLM: {'status': 'ok', 'calls': 100, 'ok': 100, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 27, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 89, 'ok': 89, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 27, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 89}, 'backlog': {'ai_relevance': {'before': 42, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 42, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 100
- Enrichment: 11
- Publish: 89

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.07
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 13.51
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 229.16
- persist_llm_cache: 0.27