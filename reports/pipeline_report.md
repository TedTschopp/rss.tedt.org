# Pipeline Report

- Timestamp: 2026-09-22T16:14:58.530400Z
- Sources configured: 43
- Raw items: 2117
- Stories: 2059
- Clusters: 2030
- LLM: {'status': 'ok', 'calls': 179, 'ok': 179, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 70, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 168, 'ok': 168, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 70, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 168}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 179
- Enrichment: 11
- Publish: 168

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.83
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 16.14
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 506.59
- persist_llm_cache: 0.21