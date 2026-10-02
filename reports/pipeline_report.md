# Pipeline Report

- Timestamp: 2026-10-02T04:03:05.407315Z
- Sources configured: 43
- Raw items: 4652
- Stories: 3082
- Clusters: 3054
- LLM: {'status': 'ok', 'calls': 417, 'ok': 417, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 174, 'importance': 172, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}}}, 'publish': {'status': 'ok', 'calls': 391, 'ok': 391, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 174, 'importance': 172, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 391}, 'backlog': {'ai_relevance': {'before': 174, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}, 'ai_relevance': {'before': 174, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 417
- Enrichment: 26
- Publish: 391

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 22
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.63
- normalize: 0.19
- dedupe: 0.10
- llm_enrich: 30.06
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.52
- publish: 990.10
- persist_llm_cache: 0.22