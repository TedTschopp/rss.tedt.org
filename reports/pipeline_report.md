# Pipeline Report

- Timestamp: 2026-07-30T09:02:17.555371Z
- Sources configured: 43
- Raw items: 1831
- Stories: 1789
- Clusters: 1758
- LLM: {'status': 'ok', 'calls': 105, 'ok': 105, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 31, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 94, 'ok': 94, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 31, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 94}, 'backlog': {'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 105
- Enrichment: 11
- Publish: 94

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.04
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 16.60
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 439.36
- persist_llm_cache: 0.22