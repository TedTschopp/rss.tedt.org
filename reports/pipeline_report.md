# Pipeline Report

- Timestamp: 2026-10-29T04:01:26.709902Z
- Sources configured: 43
- Raw items: 2129
- Stories: 2073
- Clusters: 2047
- LLM: {'status': 'degraded', 'calls': 207, 'ok': 203, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 81, 'importance': 55, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}}}, 'publish': {'status': 'degraded', 'calls': 181, 'ok': 177, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 81, 'importance': 55, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 181}, 'backlog': {'ai_relevance': {'before': 81, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 4}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}, 'ai_relevance': {'before': 81, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 4}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 26}

## LLM Calls
- Total: 207
- Enrichment: 26
- Publish: 181

## Enrichment Backlog
- Remaining: 26
- embeddings: 0
- summaries: 22
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.64
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 33.83
- cluster: 0.24
- score: 0.03
- write_intermediate_outputs: 0.25
- publish: 1370.31
- persist_llm_cache: 0.22