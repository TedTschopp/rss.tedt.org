# Pipeline Report

- Timestamp: 2026-08-30T08:13:52.302418Z
- Sources configured: 43
- Raw items: 1843
- Stories: 1818
- Clusters: 1791
- LLM: {'status': 'degraded', 'calls': 101, 'ok': 99, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 90, 'ok': 88, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 90}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 101
- Enrichment: 11
- Publish: 90

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.55
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 16.09
- cluster: 0.20
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 404.41
- persist_llm_cache: 0.14