# Pipeline Report

- Timestamp: 2026-07-15T07:55:00.121469Z
- Sources configured: 43
- Raw items: 1691
- Stories: 1657
- Clusters: 1593
- LLM: {'status': 'degraded', 'calls': 746, 'ok': 744, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 147, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 99, 'ok': 99, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 142, 'remaining': 0}, 'summaries': {'before': 97, 'remaining': 0}}}, 'publish': {'status': 'degraded', 'calls': 647, 'ok': 645, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 147, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 647}, 'backlog': {'ai_relevance': {'before': 340, 'remaining': 90}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 348, 'remaining': 98}}, 'backlog_remaining': 190}}, 'backlog': {'embeddings': {'before': 142, 'remaining': 0}, 'summaries': {'before': 97, 'remaining': 0}, 'ai_relevance': {'before': 340, 'remaining': 90}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 348, 'remaining': 98}}, 'backlog_remaining': 190}

## LLM Calls
- Total: 746
- Enrichment: 99
- Publish: 647

## Enrichment Backlog
- Remaining: 190
- embeddings: 0
- summaries: 0
- ai_relevance: 90
- importance: 2
- output_cleanup: 98

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.37
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 99.68
- cluster: 0.38
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 747.40
- persist_llm_cache: 0.28