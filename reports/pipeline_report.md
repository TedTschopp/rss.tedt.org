# Pipeline Report

- Timestamp: 2026-11-01T03:48:50.010929Z
- Sources configured: 43
- Raw items: 2103
- Stories: 2056
- Clusters: 2030
- LLM: {'status': 'degraded', 'calls': 154, 'ok': 151, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 33, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 33, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'degraded', 'calls': 128, 'ok': 125, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 33, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 128}, 'backlog': {'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 33, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 154
- Enrichment: 26
- Publish: 128

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.73
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 27.16
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.33
- publish: 757.68
- persist_llm_cache: 0.24