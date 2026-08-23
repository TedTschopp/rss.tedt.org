# Pipeline Report

- Timestamp: 2026-08-23T03:55:28.086367Z
- Sources configured: 43
- Raw items: 1876
- Stories: 1850
- Clusters: 1821
- LLM: {'status': 'ok', 'calls': 137, 'ok': 137, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 20, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'ok', 'calls': 111, 'ok': 111, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 20, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 111}, 'backlog': {'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 137
- Enrichment: 26
- Publish: 111

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.11
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 32.15
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 332.15
- persist_llm_cache: 0.21