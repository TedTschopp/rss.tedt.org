# Pipeline Report

- Timestamp: 2026-09-05T03:55:35.610952Z
- Sources configured: 43
- Raw items: 2392
- Stories: 2271
- Clusters: 2240
- LLM: {'status': 'ok', 'calls': 280, 'ok': 280, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 119, 'importance': 91, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'ok', 'calls': 254, 'ok': 254, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 119, 'importance': 91, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 254}, 'backlog': {'ai_relevance': {'before': 119, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 119, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 280
- Enrichment: 26
- Publish: 254

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.05
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 40.07
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.25
- publish: 842.99
- persist_llm_cache: 0.15