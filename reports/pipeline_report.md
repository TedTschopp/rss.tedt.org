# Pipeline Report

- Timestamp: 2026-10-27T04:02:14.866169Z
- Sources configured: 43
- Raw items: 2074
- Stories: 2031
- Clusters: 2004
- LLM: {'status': 'degraded', 'calls': 180, 'ok': 177, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 42, 'output_cleanup': 42}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 154, 'ok': 151, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 42, 'output_cleanup': 42}, 'by_model': {'openai/gpt-4.1-mini': 154}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 24}

## LLM Calls
- Total: 180
- Enrichment: 26
- Publish: 154

## Enrichment Backlog
- Remaining: 24
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 39.23
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 31.93
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.20
- publish: 851.24
- persist_llm_cache: 0.25