# Pipeline Report

- Timestamp: 2026-07-20T10:50:57.671341Z
- Sources configured: 43
- Raw items: 1829
- Stories: 1784
- Clusters: 1755
- LLM: {'status': 'ok', 'calls': 111, 'ok': 111, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 37, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 100, 'ok': 100, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 37, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 100}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 111
- Enrichment: 11
- Publish: 100

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.84
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 16.84
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.16
- publish: 479.80
- persist_llm_cache: 0.15