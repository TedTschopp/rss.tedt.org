# Pipeline Report

- Timestamp: 2026-09-22T08:15:16.212241Z
- Sources configured: 43
- Raw items: 4668
- Stories: 3412
- Clusters: 3384
- LLM: {'status': 'ok', 'calls': 180, 'ok': 180, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 169, 'ok': 169, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 169}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 180
- Enrichment: 11
- Publish: 169

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.56
- normalize: 0.20
- dedupe: 0.10
- llm_enrich: 16.36
- cluster: 0.21
- score: 0.03
- write_intermediate_outputs: 0.54
- publish: 445.01
- persist_llm_cache: 0.19