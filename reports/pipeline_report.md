# Pipeline Report

- Timestamp: 2026-10-11T08:10:26.078469Z
- Sources configured: 43
- Raw items: 2107
- Stories: 2068
- Clusters: 2039
- LLM: {'status': 'ok', 'calls': 108, 'ok': 108, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 31, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 17, 'remaining': 0}, 'summaries': {'before': 17, 'remaining': 7}}}, 'publish': {'status': 'ok', 'calls': 97, 'ok': 97, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 31, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 97}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 17, 'remaining': 0}, 'summaries': {'before': 17, 'remaining': 7}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 7}

## LLM Calls
- Total: 108
- Enrichment: 11
- Publish: 97

## Enrichment Backlog
- Remaining: 7
- embeddings: 0
- summaries: 7
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.99
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 12.26
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 172.16
- persist_llm_cache: 0.22