# Pipeline Report

- Timestamp: 2026-10-30T03:43:56.936113Z
- Sources configured: 43
- Raw items: 2105
- Stories: 2054
- Clusters: 2026
- LLM: {'status': 'ok', 'calls': 133, 'ok': 133, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 22, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'ok', 'calls': 107, 'ok': 107, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 22, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 107}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 133
- Enrichment: 26
- Publish: 107

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.72
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 28.79
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 329.07
- persist_llm_cache: 0.22