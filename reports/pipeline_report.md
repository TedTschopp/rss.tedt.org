# Pipeline Report

- Timestamp: 2026-07-26T00:31:38.805895Z
- Sources configured: 43
- Raw items: 1856
- Stories: 1810
- Clusters: 1781
- LLM: {'status': 'ok', 'calls': 106, 'ok': 106, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 26, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 95, 'ok': 95, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 26, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 95}, 'backlog': {'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 106
- Enrichment: 11
- Publish: 95

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.03
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 13.44
- cluster: 0.21
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 285.96
- persist_llm_cache: 0.16