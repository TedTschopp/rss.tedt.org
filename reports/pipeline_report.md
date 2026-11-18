# Pipeline Report

- Timestamp: 2026-11-18T12:23:40.552867Z
- Sources configured: 43
- Raw items: 2198
- Stories: 2138
- Clusters: 2108
- LLM: {'status': 'degraded', 'calls': 270, 'ok': 269, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 109, 'importance': 85, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 244, 'ok': 243, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 109, 'importance': 85, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 244}, 'backlog': {'ai_relevance': {'before': 109, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 109, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 270
- Enrichment: 26
- Publish: 244

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.02
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 34.96
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 979.63
- persist_llm_cache: 0.27