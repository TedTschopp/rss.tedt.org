# Pipeline Report

- Timestamp: 2026-09-07T03:49:57.997516Z
- Sources configured: 43
- Raw items: 1917
- Stories: 1868
- Clusters: 1839
- LLM: {'status': 'ok', 'calls': 148, 'ok': 148, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 25, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}}}, 'publish': {'status': 'ok', 'calls': 122, 'ok': 122, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 25, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 122}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}, 'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 18}

## LLM Calls
- Total: 148
- Enrichment: 26
- Publish: 122

## Enrichment Backlog
- Remaining: 18
- embeddings: 0
- summaries: 18
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.32
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 35.96
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 376.69
- persist_llm_cache: 0.21