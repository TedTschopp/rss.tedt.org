# Pipeline Report

- Timestamp: 2026-09-18T08:15:04.371444Z
- Sources configured: 43
- Raw items: 3670
- Stories: 2509
- Clusters: 2479
- LLM: {'status': 'ok', 'calls': 184, 'ok': 184, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 173, 'ok': 173, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 173}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 184
- Enrichment: 11
- Publish: 173

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.01
- normalize: 0.20
- dedupe: 0.10
- llm_enrich: 16.55
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.40
- publish: 440.53
- persist_llm_cache: 0.22