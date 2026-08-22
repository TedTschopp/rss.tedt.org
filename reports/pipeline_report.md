# Pipeline Report

- Timestamp: 2026-08-22T08:11:42.255836Z
- Sources configured: 43
- Raw items: 1926
- Stories: 1879
- Clusters: 1850
- LLM: {'status': 'ok', 'calls': 106, 'ok': 106, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 27, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 17, 'remaining': 0}, 'summaries': {'before': 17, 'remaining': 7}}}, 'publish': {'status': 'ok', 'calls': 95, 'ok': 95, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 27, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 95}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 17, 'remaining': 0}, 'summaries': {'before': 17, 'remaining': 7}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 7}

## LLM Calls
- Total: 106
- Enrichment: 11
- Publish: 95

## Enrichment Backlog
- Remaining: 7
- embeddings: 0
- summaries: 7
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.92
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 16.11
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.16
- publish: 266.32
- persist_llm_cache: 0.14