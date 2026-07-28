# Pipeline Report

- Timestamp: 2026-07-28T16:42:14.787578Z
- Sources configured: 43
- Raw items: 1949
- Stories: 1897
- Clusters: 1869
- LLM: {'status': 'ok', 'calls': 155, 'ok': 155, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 58, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 144, 'ok': 144, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 58, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 144}, 'backlog': {'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 155
- Enrichment: 11
- Publish: 144

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.44
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 38.33
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 513.80
- persist_llm_cache: 0.21