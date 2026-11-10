# Pipeline Report

- Timestamp: 2026-11-10T12:01:48.629802Z
- Sources configured: 43
- Raw items: 6146
- Stories: 3819
- Clusters: 3789
- LLM: {'status': 'degraded', 'calls': 464, 'ok': 463, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 193, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}}}, 'publish': {'status': 'degraded', 'calls': 438, 'ok': 437, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 193, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 438}, 'backlog': {'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}, 'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 24}

## LLM Calls
- Total: 464
- Enrichment: 26
- Publish: 438

## Enrichment Backlog
- Remaining: 24
- embeddings: 0
- summaries: 23
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.56
- normalize: 0.27
- dedupe: 0.14
- llm_enrich: 32.69
- cluster: 0.23
- score: 0.03
- write_intermediate_outputs: 0.64
- publish: 1602.80
- persist_llm_cache: 0.31