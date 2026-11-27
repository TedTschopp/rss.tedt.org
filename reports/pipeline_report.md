# Pipeline Report

- Timestamp: 2026-11-27T07:21:37.241519Z
- Sources configured: 43
- Raw items: 3192
- Stories: 2695
- Clusters: 2662
- LLM: {'status': 'ok', 'calls': 188, 'ok': 188, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 78, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 177, 'ok': 177, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 78, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 177}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 188
- Enrichment: 11
- Publish: 177

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.00
- normalize: 0.11
- dedupe: 0.07
- llm_enrich: 17.03
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.37
- publish: 544.15
- persist_llm_cache: 0.28