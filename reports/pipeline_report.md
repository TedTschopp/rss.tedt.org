# Pipeline Report

- Timestamp: 2026-09-16T00:18:30.794161Z
- Sources configured: 43
- Raw items: 2044
- Stories: 1992
- Clusters: 1962
- LLM: {'status': 'ok', 'calls': 154, 'ok': 154, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 56, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 143, 'ok': 143, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 56, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 143}, 'backlog': {'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 154
- Enrichment: 11
- Publish: 143

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.71
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 15.85
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 363.49
- persist_llm_cache: 0.17