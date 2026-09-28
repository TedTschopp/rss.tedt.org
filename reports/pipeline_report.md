# Pipeline Report

- Timestamp: 2026-09-28T03:55:50.821440Z
- Sources configured: 43
- Raw items: 1964
- Stories: 1926
- Clusters: 1892
- LLM: {'status': 'ok', 'calls': 192, 'ok': 192, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 39, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'ok', 'calls': 166, 'ok': 166, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 39, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 166}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 192
- Enrichment: 26
- Publish: 166

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.23
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 32.15
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 303.28
- persist_llm_cache: 0.22