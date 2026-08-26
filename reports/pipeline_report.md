# Pipeline Report

- Timestamp: 2026-08-26T08:25:49.382634Z
- Sources configured: 43
- Raw items: 3723
- Stories: 2528
- Clusters: 2499
- LLM: {'status': 'ok', 'calls': 181, 'ok': 181, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 74, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 170, 'ok': 170, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 74, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 170}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 181
- Enrichment: 11
- Publish: 170

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.08
- normalize: 0.19
- dedupe: 0.10
- llm_enrich: 23.54
- cluster: 0.29
- score: 0.03
- write_intermediate_outputs: 0.41
- publish: 664.23
- persist_llm_cache: 0.22