# Pipeline Report

- Timestamp: 2026-08-24T08:24:35.550082Z
- Sources configured: 43
- Raw items: 3289
- Stories: 2362
- Clusters: 2333
- LLM: {'status': 'ok', 'calls': 190, 'ok': 190, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 79, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 179, 'ok': 179, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 79, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 179}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 190
- Enrichment: 11
- Publish: 179

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.08
- normalize: 0.18
- dedupe: 0.09
- llm_enrich: 18.80
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 520.76
- persist_llm_cache: 0.22