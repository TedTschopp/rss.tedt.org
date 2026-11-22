# Pipeline Report

- Timestamp: 2026-11-22T12:02:00.050594Z
- Sources configured: 43
- Raw items: 2151
- Stories: 2103
- Clusters: 2075
- LLM: {'status': 'ok', 'calls': 199, 'ok': 199, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 52, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}}}, 'publish': {'status': 'ok', 'calls': 173, 'ok': 173, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 52, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 173}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 199
- Enrichment: 26
- Publish: 173

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 22
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.93
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 31.40
- cluster: 0.19
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 657.26
- persist_llm_cache: 0.18