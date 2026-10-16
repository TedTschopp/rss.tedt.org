# Pipeline Report

- Timestamp: 2026-10-16T04:00:55.449597Z
- Sources configured: 43
- Raw items: 4270
- Stories: 2953
- Clusters: 2923
- LLM: {'status': 'ok', 'calls': 403, 'ok': 403, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 168, 'importance': 165, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'ok', 'calls': 377, 'ok': 377, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 168, 'importance': 165, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 377}, 'backlog': {'ai_relevance': {'before': 168, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 168, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 403
- Enrichment: 26
- Publish: 377

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.70
- normalize: 0.25
- dedupe: 0.12
- llm_enrich: 30.30
- cluster: 0.29
- score: 0.03
- write_intermediate_outputs: 0.48
- publish: 901.03
- persist_llm_cache: 0.24