import hashlib
import json
import time
from typing import Any, cast

import requests


class GitHubModelsClient:
    def __init__(self, token: str, endpoint: str = "https://models.github.ai/inference", timeout_sec: int = 25):
        self.token = token
        self.endpoint = endpoint.rstrip("/")
        self.timeout_sec = timeout_sec
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    @staticmethod
    def input_hash(payload: dict[str, Any]) -> str:
        raw = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()

    def embed(self, texts: list[str], model: str = "openai/text-embedding-3-small") -> dict[str, Any]:
        payload: dict[str, Any] = {"model": model, "input": texts}
        started = time.perf_counter()
        response = self.session.post(f"{self.endpoint}/embeddings", json=payload, timeout=self.timeout_sec)
        latency_ms = int((time.perf_counter() - started) * 1000)
        response.raise_for_status()
        data = response.json()
        vectors = [item.get("embedding", []) for item in data.get("data", [])]
        usage = data.get("usage", {})
        return {"vectors": vectors, "usage": usage, "latency_ms": latency_ms, "model": model, "input_hash": self.input_hash(payload)}

    def summarize(self, title: str, summary: str, model: str = "openai/gpt-4.1-mini") -> dict[str, Any]:
        schema: dict[str, Any] = {
            "type": "json_schema",
            "json_schema": {
                "name": "story_enrichment",
                "schema": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string"},
                        "topics": {"type": "array", "items": {"type": "string"}},
                        "entities": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["summary", "topics", "entities"],
                    "additionalProperties": False
                }
            }
        }
        payload: dict[str, Any] = {
            "model": model,
            "messages": [
                {"role": "system", "content": "Summarize technology news in neutral language."},
                {"role": "user", "content": f"Title: {title}\n\nContext: {summary}"}
            ],
            "temperature": 0.2,
            "response_format": schema,
        }

        started = time.perf_counter()
        response = self.session.post(f"{self.endpoint}/chat/completions", json=payload, timeout=self.timeout_sec)
        latency_ms = int((time.perf_counter() - started) * 1000)
        response.raise_for_status()
        data: dict[str, Any] = response.json()
        choices = data.get("choices")
        first_choice: dict[str, Any] = {}
        if isinstance(choices, list) and choices and isinstance(choices[0], dict):
            first_choice = cast(dict[str, Any], choices[0])
        message = first_choice.get("message", {})
        message_map: dict[str, Any] = cast(dict[str, Any], message) if isinstance(message, dict) else {}
        content_raw = message_map.get("content", "{}")
        content = str(content_raw).strip()
        parsed: dict[str, Any] = json.loads(content)
        return {
            "summary": parsed.get("summary", ""),
            "topics": parsed.get("topics", []),
            "entities": parsed.get("entities", []),
            "usage": data.get("usage", {}),
            "latency_ms": latency_ms,
            "model": model,
            "input_hash": self.input_hash(payload),
        }
