# Pipeline Report

- Timestamp: 2026-07-16T01:54:33.628512Z
- Sources configured: 43
- Raw items: 1866
- Stories: 1805
- Clusters: 1758
- LLM: {'status': 'ok', 'calls': 132, 'ok': 132, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 43, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 121, 'ok': 121, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 43, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 121}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 132
- Enrichment: 11
- Publish: 121

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.12
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 16.32
- cluster: 0.33
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 470.70
- persist_llm_cache: 0.24