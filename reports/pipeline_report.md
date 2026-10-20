# Pipeline Report

- Timestamp: 2026-10-20T08:15:36.399735Z
- Sources configured: 43
- Raw items: 5640
- Stories: 3551
- Clusters: 3520
- LLM: {'status': 'ok', 'calls': 186, 'ok': 186, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 175, 'ok': 175, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 175}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 186
- Enrichment: 11
- Publish: 175

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.14
- normalize: 0.37
- dedupe: 0.18
- llm_enrich: 13.72
- cluster: 0.33
- score: 0.04
- write_intermediate_outputs: 0.64
- publish: 495.51
- persist_llm_cache: 0.26