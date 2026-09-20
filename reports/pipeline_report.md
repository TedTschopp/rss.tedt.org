# Pipeline Report

- Timestamp: 2026-09-20T03:50:33.821782Z
- Sources configured: 43
- Raw items: 1939
- Stories: 1905
- Clusters: 1877
- LLM: {'status': 'degraded', 'calls': 180, 'ok': 179, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 41, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'degraded', 'calls': 154, 'ok': 153, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 41, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 154}, 'backlog': {'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 180
- Enrichment: 26
- Publish: 154

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.60
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 30.19
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 458.80
- persist_llm_cache: 0.21