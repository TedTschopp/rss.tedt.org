# Pipeline Report

- Timestamp: 2026-11-07T05:07:33.154684Z
- Sources configured: 43
- Raw items: 2121
- Stories: 2065
- Clusters: 2036
- LLM: {'status': 'ok', 'calls': 101, 'ok': 101, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 28, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 90, 'ok': 90, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 28, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 90}, 'backlog': {'ai_relevance': {'before': 42, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 42, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 101
- Enrichment: 11
- Publish: 90

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.94
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 14.71
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 286.36
- persist_llm_cache: 0.27