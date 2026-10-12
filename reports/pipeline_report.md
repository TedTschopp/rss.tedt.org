# Pipeline Report

- Timestamp: 2026-10-12T08:24:18.304644Z
- Sources configured: 43
- Raw items: 1912
- Stories: 1873
- Clusters: 1847
- LLM: {'status': 'ok', 'calls': 80, 'ok': 80, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 29, 'importance': 20, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 69, 'ok': 69, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 29, 'importance': 20, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 69}, 'backlog': {'ai_relevance': {'before': 29, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 29, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 80
- Enrichment: 11
- Publish: 69

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 4.75
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 15.66
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 141.80
- persist_llm_cache: 0.21