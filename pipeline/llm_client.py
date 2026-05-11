import hashlib
import json
import time
from pathlib import Path
from typing import Any, cast

import requests


BUSINESS_IMPACT_TAGS = {1: "[ ~ ]", 2: "[ * ]", 3: "[ ! ]"}
TECHNICAL_IMPACT_TAGS = {1: "[ ◻ ]", 2: "[ ◼ ]", 3: "[ ⬢ ]"}
REASON_CODE_VALUES = [
    "ARCH",
    "PLAT",
    "ID",
    "SEC",
    "DATA",
    "GOV",
    "REG",
    "COST",
    "OPS",
    "ECO",
    "PROC",
    "CX",
    "COMP",
    "LABOR",
    "GEO",
    "HYPE",
]


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    items = cast(list[Any], value)
    result: list[str] = []
    for item in items:
        text = str(item).strip()
        if text:
            result.append(text)
    return result


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
        self.prompts_dir = Path("prompts")

    def _load_text_prompt(self, filename: str, fallback: str) -> str:
        path = self.prompts_dir / filename
        if not path.exists():
            return fallback
        content = path.read_text(encoding="utf-8").strip()
        return content or fallback

    def _load_json_prompt(self, filename: str, fallback: dict[str, Any]) -> dict[str, Any]:
        path = self.prompts_dir / filename
        if not path.exists():
            return fallback
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(payload, dict):
                return cast(dict[str, Any], payload)
            return fallback
        except Exception:
            return fallback

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
        default_schema: dict[str, Any] = {
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
        schema = self._load_json_prompt("summary_schema.json", default_schema)
        system_prompt = self._load_text_prompt("summary_system.txt", "Summarize technology news in neutral language.")
        user_template = self._load_text_prompt("summary_user.txt", "Title: {title}\n\nContext: {summary}")
        user_prompt = user_template.format(title=title, summary=summary)

        payload: dict[str, Any] = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
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

    def check_ai_relevance(
        self,
        title: str,
        summary: str,
        rubric_markdown: str,
        model: str = "openai/gpt-4.1-mini",
        article: str = "",
    ) -> dict[str, Any]:
        default_schema: dict[str, Any] = {
            "type": "json_schema",
            "json_schema": {
                "name": "ai_relevance_gate",
                "schema": {
                    "type": "object",
                    "properties": {
                        "is_ai_related": {"type": "boolean"},
                        "decision": {"type": "string", "enum": ["proceed", "skip"]},
                        "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
                        "primary_ai_topic": {"type": "string"},
                        "rationale": {"type": "string"},
                        "evidence": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "is_ai_related",
                        "decision",
                        "confidence",
                        "primary_ai_topic",
                        "rationale",
                        "evidence",
                    ],
                    "additionalProperties": False,
                },
            },
        }

        schema = self._load_json_prompt("ai_relevance_schema.json", default_schema)
        system_prompt = self._load_text_prompt(
            "ai_relevance_system.txt",
            "You are a strict AI-news relevance classifier. Return only JSON matching the schema.",
        )
        user_template = self._load_text_prompt(
            "ai_relevance_user.txt",
            "Rubric:\n{rubric}\n\nStory Title: {title}\n\nStory Summary: {summary}\n\nArticle Content:\n{article}",
        )
        user_prompt = user_template.format(title=title, summary=summary, rubric=rubric_markdown, article=article)

        payload: dict[str, Any] = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.0,
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
        is_ai_related = bool(parsed.get("is_ai_related"))
        decision = str(parsed.get("decision") or ("proceed" if is_ai_related else "skip"))

        return {
            "is_ai_related": is_ai_related,
            "decision": decision if decision in {"proceed", "skip"} else ("proceed" if is_ai_related else "skip"),
            "confidence": parsed.get("confidence", ""),
            "primary_ai_topic": parsed.get("primary_ai_topic", ""),
            "rationale": parsed.get("rationale", ""),
            "evidence": _string_list(parsed.get("evidence")),
            "usage": data.get("usage", {}),
            "latency_ms": latency_ms,
            "model": model,
            "input_hash": self.input_hash(payload),
        }

    def grade_importance(
        self,
        title: str,
        summary: str,
        rubric_markdown: str,
        model: str = "openai/gpt-4.1-mini",
        article: str = "",
    ) -> dict[str, Any]:
        default_schema: dict[str, Any] = {
            "type": "json_schema",
            "json_schema": {
                "name": "importance_grading",
                "schema": {
                    "type": "object",
                    "properties": {
                        "business_level": {"type": "integer", "minimum": 1, "maximum": 3},
                        "technical_level": {"type": "integer", "minimum": 1, "maximum": 3},
                        "business_impact": {"type": "string", "enum": list(BUSINESS_IMPACT_TAGS.values())},
                        "technical_impact": {"type": "string", "enum": list(TECHNICAL_IMPACT_TAGS.values())},
                        "risk_impact": {"type": "string", "enum": ["R1", "R2", "R3"]},
                        "enterprise_readiness": {"type": "string", "enum": ["ER0", "ER1", "ER2", "ER3", "ER4"]},
                        "labor_workflow_impact": {"type": "string", "enum": ["L0", "L1", "L2", "L3"]},
                        "confidence": {"type": "string", "enum": ["C1", "C2", "C3", "C4"]},
                        "attention_priority": {"type": "string", "enum": ["P0", "P1", "P2", "P3", "P4", "P5"]},
                        "development_summary": {"type": "string"},
                        "reason_codes": {"type": "array", "items": {"type": "string", "enum": REASON_CODE_VALUES}},
                        "recommended_action": {"type": "string"},
                        "rationale": {"type": "string"},
                        "watch_items": {"type": "array", "items": {"type": "string"}},
                        "business_rationale": {"type": "string"},
                        "technical_rationale": {"type": "string"},
                    },
                    "required": [
                        "business_level",
                        "technical_level",
                        "business_impact",
                        "technical_impact",
                        "risk_impact",
                        "enterprise_readiness",
                        "labor_workflow_impact",
                        "confidence",
                        "attention_priority",
                        "development_summary",
                        "reason_codes",
                        "recommended_action",
                        "rationale",
                        "watch_items",
                        "business_rationale",
                        "technical_rationale",
                    ],
                    "additionalProperties": False,
                },
            },
        }

        schema = self._load_json_prompt("importance_schema.json", default_schema)
        system_prompt = self._load_text_prompt(
            "importance_system.txt",
            "You are a precise enterprise technology analyst. Grade the story using the provided rubric.",
        )
        user_template = self._load_text_prompt(
            "importance_user.txt",
            "Rubric:\n{rubric}\n\nStory Title: {title}\n\nStory Context: {summary}\n\nArticle Content:\n{article}",
        )
        user_prompt = user_template.format(title=title, summary=summary, rubric=rubric_markdown, article=article)

        payload: dict[str, Any] = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.0,
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
        business_level = parsed.get("business_level")
        technical_level = parsed.get("technical_level")
        try:
            business_level_int = int(str(business_level or "0"))
        except Exception:
            business_level_int = 0
        try:
            technical_level_int = int(str(technical_level or "0"))
        except Exception:
            technical_level_int = 0

        return {
            "business_level": business_level,
            "technical_level": technical_level,
            "business_impact": parsed.get("business_impact") or BUSINESS_IMPACT_TAGS.get(business_level_int, ""),
            "technical_impact": parsed.get("technical_impact") or TECHNICAL_IMPACT_TAGS.get(technical_level_int, ""),
            "risk_impact": parsed.get("risk_impact", ""),
            "enterprise_readiness": parsed.get("enterprise_readiness", ""),
            "labor_workflow_impact": parsed.get("labor_workflow_impact", ""),
            "confidence": parsed.get("confidence", ""),
            "attention_priority": parsed.get("attention_priority", ""),
            "development_summary": parsed.get("development_summary", ""),
            "reason_codes": _string_list(parsed.get("reason_codes")),
            "recommended_action": parsed.get("recommended_action", ""),
            "rationale": parsed.get("rationale", ""),
            "watch_items": _string_list(parsed.get("watch_items")),
            "business_rationale": parsed.get("business_rationale", ""),
            "technical_rationale": parsed.get("technical_rationale", ""),
            "usage": data.get("usage", {}),
            "latency_ms": latency_ms,
            "model": model,
            "input_hash": self.input_hash(payload),
        }
