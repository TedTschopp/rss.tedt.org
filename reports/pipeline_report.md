# Pipeline Report

- Timestamp: 2026-10-18T00:16:35.196234Z
- Sources configured: 43
- Raw items: 2051
- Stories: 2008
- Clusters: 1980
- LLM: {'status': 'ok', 'calls': 112, 'ok': 112, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 28, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 101, 'ok': 101, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 28, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 101}, 'backlog': {'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 112
- Enrichment: 11
- Publish: 101

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.15
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 12.85
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 234.99
- persist_llm_cache: 0.25