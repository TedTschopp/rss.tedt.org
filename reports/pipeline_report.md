# Pipeline Report

- Timestamp: 2026-10-21T00:19:12.337931Z
- Sources configured: 43
- Raw items: 2127
- Stories: 2073
- Clusters: 2043
- LLM: {'status': 'ok', 'calls': 154, 'ok': 154, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 54, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 143, 'ok': 143, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 54, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 143}, 'backlog': {'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 154
- Enrichment: 11
- Publish: 143

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 18.06
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 18.14
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.32
- publish: 394.17
- persist_llm_cache: 0.26