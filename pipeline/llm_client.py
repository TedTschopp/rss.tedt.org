import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any, cast
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

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

HEADLINE_INSTRUCTIONS_PATH = Path("Docs/design/Prompts-Needed/Headline-Generation-Instructions.md")
ARTICLE_SUMMARY_INSTRUCTIONS_PATH = Path("Docs/design/Prompts-Needed/Article-Summary.md")
TITLE_OUTPUT_CONTRACT = (
    "Application output contract: Use the standard headline instructions as editorial policy. "
    "Return JSON matching the provided schema with exactly one field named title. "
    "The title value must contain only the rewritten headline, with no alternatives, explanations, scoring, Markdown, HTML, or XML."
)
DESCRIPTION_OUTPUT_CONTRACT = (
    "Application output contract: Use the standard article summary instructions as editorial policy. "
    "Return JSON matching the provided schema with exactly one field named description. "
    "The description value must contain only the final formatted description, with no labels, alternatives, explanations, scoring, Markdown, HTML, or XML. "
    "When multiple paragraphs are warranted, preserve blank lines between paragraphs inside the description value."
)
OUTPUT_CLEANUP_OUTPUT_CONTRACT = (
    "Application output contract: Use the headline instructions for the title and the article summary instructions for the description. "
    "Return JSON matching the provided schema with exactly two fields: title and description. "
    "Do not include alternatives, explanations, scoring, Markdown, HTML, or XML."
)

OPENAI_TOKEN_EXCHANGE_URL = "https://auth.openai.com/oauth/token"
OPENAI_TOKEN_EXCHANGE_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:token-exchange"
OPENAI_SUBJECT_TOKEN_TYPE_JWT = "urn:ietf:params:oauth:token-type:jwt"


class LLMProviderConfigError(RuntimeError):
    pass


def normalize_llm_provider(value: Any) -> str:
    provider = str(value or "github_models").strip().lower().replace("-", "_")
    if provider in {"openai", "openai_api", "openai_wif"}:
        return "openai"
    if provider in {"github", "github_models", "gh_models", "models"}:
        return "github_models"
    return provider or "github_models"


def _url_with_audience(url: str, audience: str) -> str:
    parsed = urlsplit(url)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    query["audience"] = audience
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urlencode(query), parsed.fragment))


class OpenAIWorkloadIdentityTokenProvider:
    def __init__(
        self,
        *,
        identity_provider_id: str,
        service_account_id: str,
        audience: str,
        request_url: str,
        request_token: str,
        client_id: str | None = None,
        token_exchange_url: str = OPENAI_TOKEN_EXCHANGE_URL,
        session: requests.Session | None = None,
        timeout_sec: int = 25,
        refresh_buffer_sec: int = 1200,
        clock=None,
    ):
        self.identity_provider_id = identity_provider_id
        self.service_account_id = service_account_id
        self.audience = audience
        self.request_url = request_url
        self.request_token = request_token
        self.client_id = client_id
        self.token_exchange_url = token_exchange_url
        self.session = session or requests.Session()
        self.timeout_sec = timeout_sec
        self.refresh_buffer_sec = refresh_buffer_sec
        self.clock = clock or time.time
        self._access_token = ""
        self._expires_at = 0.0

    @classmethod
    def from_env(
        cls,
        environ: dict[str, str] | None = None,
        *,
        session: requests.Session | None = None,
        timeout_sec: int = 25,
    ) -> "OpenAIWorkloadIdentityTokenProvider":
        env = environ or os.environ
        required = {
            "OPENAI_WIF_AUDIENCE": env.get("OPENAI_WIF_AUDIENCE", "").strip(),
            "OPENAI_IDENTITY_PROVIDER_ID": env.get("OPENAI_IDENTITY_PROVIDER_ID", "").strip(),
            "OPENAI_SERVICE_ACCOUNT_ID": env.get("OPENAI_SERVICE_ACCOUNT_ID", "").strip(),
            "ACTIONS_ID_TOKEN_REQUEST_URL": env.get("ACTIONS_ID_TOKEN_REQUEST_URL", "").strip(),
            "ACTIONS_ID_TOKEN_REQUEST_TOKEN": env.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "").strip(),
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise LLMProviderConfigError(
                "missing OpenAI workload identity environment variables: " + ", ".join(missing)
            )
        return cls(
            identity_provider_id=required["OPENAI_IDENTITY_PROVIDER_ID"],
            service_account_id=required["OPENAI_SERVICE_ACCOUNT_ID"],
            audience=required["OPENAI_WIF_AUDIENCE"],
            request_url=required["ACTIONS_ID_TOKEN_REQUEST_URL"],
            request_token=required["ACTIONS_ID_TOKEN_REQUEST_TOKEN"],
            client_id=env.get("OPENAI_WIF_CLIENT_ID", "").strip() or None,
            session=session,
            timeout_sec=timeout_sec,
        )

    def _request_subject_token(self) -> str:
        response = self.session.get(
            _url_with_audience(self.request_url, self.audience),
            headers={
                "Authorization": f"bearer {self.request_token}",
                "Accept": "application/json",
            },
            timeout=self.timeout_sec,
        )
        response.raise_for_status()
        data = response.json()
        token = str(data.get("value") or "").strip() if isinstance(data, dict) else ""
        if not token:
            raise LLMProviderConfigError("GitHub OIDC token response did not include a value")
        return token

    def _exchange_subject_token(self, subject_token: str) -> tuple[str, int]:
        payload: dict[str, Any] = {
            "grant_type": OPENAI_TOKEN_EXCHANGE_GRANT_TYPE,
            "subject_token": subject_token,
            "subject_token_type": OPENAI_SUBJECT_TOKEN_TYPE_JWT,
            "identity_provider_id": self.identity_provider_id,
            "service_account_id": self.service_account_id,
        }
        if self.client_id:
            payload["client_id"] = self.client_id
        response = self.session.post(
            self.token_exchange_url,
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            timeout=self.timeout_sec,
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            raise LLMProviderConfigError("OpenAI token exchange returned a non-object response")
        access_token = str(data.get("access_token") or "").strip()
        if not access_token:
            raise LLMProviderConfigError("OpenAI token exchange response did not include access_token")
        try:
            expires_in = int(data.get("expires_in") or 3600)
        except Exception:
            expires_in = 3600
        return access_token, max(1, expires_in)

    def get_token(self) -> str:
        now = float(self.clock())
        if self._access_token and now < self._expires_at - self.refresh_buffer_sec:
            return self._access_token
        subject_token = self._request_subject_token()
        access_token, expires_in = self._exchange_subject_token(subject_token)
        self._access_token = access_token
        self._expires_at = now + expires_in
        return self._access_token


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
        self.headline_instructions_path = HEADLINE_INSTRUCTIONS_PATH
        self.article_summary_instructions_path = ARTICLE_SUMMARY_INSTRUCTIONS_PATH

    def _request_model_name(self, model: str) -> str:
        return model

    def _post(self, path: str, payload: dict[str, Any]):
        return self.session.post(f"{self.endpoint}/{path.lstrip('/')}", json=payload, timeout=self.timeout_sec)

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

    def _load_text_file(self, path: Path) -> str:
        try:
            if not path.exists():
                return ""
            return path.read_text(encoding="utf-8").strip()
        except Exception:
            return ""

    def _load_title_system_prompt(self) -> str:
        application_prompt = self._load_text_prompt(
            "output_cleanup/title_system.txt",
            "Rewrite the news title in neutral language. Return only JSON matching the schema.",
        )
        headline_instructions = self._load_text_file(self.headline_instructions_path)
        if not headline_instructions:
            return application_prompt
        return "\n\n".join(
            [
                headline_instructions,
                TITLE_OUTPUT_CONTRACT,
                application_prompt,
            ]
        )

    def _load_description_system_prompt(self) -> str:
        application_prompt = self._load_text_prompt(
            "output_cleanup/description_system.txt",
            "Rewrite the news description in neutral language. Return only JSON matching the schema.",
        )
        article_summary_instructions = self._load_text_file(self.article_summary_instructions_path)
        if not article_summary_instructions:
            return application_prompt
        return "\n\n".join(
            [
                article_summary_instructions,
                DESCRIPTION_OUTPUT_CONTRACT,
                application_prompt,
            ]
        )

    def _load_output_cleanup_system_prompt(self) -> str:
        title_prompt = self._load_text_prompt(
            "output_cleanup/title_system.txt",
            "Rewrite the news title in neutral language.",
        )
        description_prompt = self._load_text_prompt(
            "output_cleanup/description_system.txt",
            "Rewrite the news description in neutral language.",
        )
        headline_instructions = self._load_text_file(self.headline_instructions_path)
        article_summary_instructions = self._load_text_file(self.article_summary_instructions_path)
        parts = [
            part
            for part in [
                headline_instructions,
                article_summary_instructions,
                OUTPUT_CLEANUP_OUTPUT_CONTRACT,
                title_prompt,
                description_prompt,
            ]
            if part
        ]
        return "\n\n".join(parts) or "Rewrite the news title and description. Return only JSON matching the schema."

    @staticmethod
    def input_hash(payload: dict[str, Any]) -> str:
        raw = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()

    def embed(self, texts: list[str], model: str = "openai/text-embedding-3-small") -> dict[str, Any]:
        payload: dict[str, Any] = {"model": self._request_model_name(model), "input": texts}
        started = time.perf_counter()
        response = self._post("embeddings", payload)
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
            "model": self._request_model_name(model),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2,
            "response_format": schema,
        }

        started = time.perf_counter()
        response = self._post("chat/completions", payload)
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

    def rewrite_output_title(
        self,
        title: str,
        summary: str,
        source_context: str,
        model: str = "openai/gpt-4.1-mini",
    ) -> dict[str, Any]:
        default_schema: dict[str, Any] = {
            "type": "json_schema",
            "json_schema": {
                "name": "output_title_rewrite",
                "schema": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                    "additionalProperties": False,
                },
            },
        }
        schema = self._load_json_prompt("output_cleanup/title_schema.json", default_schema)
        system_prompt = self._load_title_system_prompt()
        user_template = self._load_text_prompt(
            "output_cleanup/title_user.txt",
            "Original Title: {title}\n\nCurrent Description: {summary}\n\nSource Context:\n{source_context}",
        )
        user_prompt = user_template.format(title=title, summary=summary, source_context=source_context)

        payload: dict[str, Any] = {
            "model": self._request_model_name(model),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.1,
            "response_format": schema,
        }

        started = time.perf_counter()
        response = self._post("chat/completions", payload)
        latency_ms = int((time.perf_counter() - started) * 1000)
        response.raise_for_status()
        data: dict[str, Any] = response.json()
        choices = data.get("choices")
        first_choice: dict[str, Any] = {}
        if isinstance(choices, list) and choices and isinstance(choices[0], dict):
            first_choice = cast(dict[str, Any], choices[0])
        message = first_choice.get("message", {})
        message_map: dict[str, Any] = cast(dict[str, Any], message) if isinstance(message, dict) else {}
        content = str(message_map.get("content", "{}") or "{}").strip()
        parsed: dict[str, Any] = json.loads(content)
        return {
            "title": str(parsed.get("title") or title).strip(),
            "usage": data.get("usage", {}),
            "latency_ms": latency_ms,
            "model": model,
            "input_hash": self.input_hash(payload),
        }

    def rewrite_output_description(
        self,
        title: str,
        summary: str,
        source_context: str,
        model: str = "openai/gpt-4.1-mini",
    ) -> dict[str, Any]:
        default_schema: dict[str, Any] = {
            "type": "json_schema",
            "json_schema": {
                "name": "output_description_rewrite",
                "schema": {
                    "type": "object",
                    "properties": {"description": {"type": "string"}},
                    "required": ["description"],
                    "additionalProperties": False,
                },
            },
        }
        schema = self._load_json_prompt("output_cleanup/description_schema.json", default_schema)
        system_prompt = self._load_description_system_prompt()
        user_template = self._load_text_prompt(
            "output_cleanup/description_user.txt",
            "Output Title: {title}\n\nCurrent Description: {summary}\n\nSource Context:\n{source_context}",
        )
        user_prompt = user_template.format(title=title, summary=summary, source_context=source_context)

        payload: dict[str, Any] = {
            "model": self._request_model_name(model),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.1,
            "response_format": schema,
        }

        started = time.perf_counter()
        response = self._post("chat/completions", payload)
        latency_ms = int((time.perf_counter() - started) * 1000)
        response.raise_for_status()
        data: dict[str, Any] = response.json()
        choices = data.get("choices")
        first_choice: dict[str, Any] = {}
        if isinstance(choices, list) and choices and isinstance(choices[0], dict):
            first_choice = cast(dict[str, Any], choices[0])
        message = first_choice.get("message", {})
        message_map: dict[str, Any] = cast(dict[str, Any], message) if isinstance(message, dict) else {}
        content = str(message_map.get("content", "{}") or "{}").strip()
        parsed: dict[str, Any] = json.loads(content)
        return {
            "description": str(parsed.get("description") or summary).strip(),
            "usage": data.get("usage", {}),
            "latency_ms": latency_ms,
            "model": model,
            "input_hash": self.input_hash(payload),
        }

    def rewrite_output_cleanup(
        self,
        title: str,
        summary: str,
        source_context: str,
        model: str = "openai/gpt-4.1-mini",
    ) -> dict[str, Any]:
        default_schema: dict[str, Any] = {
            "type": "json_schema",
            "json_schema": {
                "name": "output_cleanup_rewrite",
                "schema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["title", "description"],
                    "additionalProperties": False,
                },
            },
        }
        schema = self._load_json_prompt("output_cleanup/combined_schema.json", default_schema)
        system_prompt = self._load_output_cleanup_system_prompt()
        user_template = self._load_text_prompt(
            "output_cleanup/combined_user.txt",
            "Original Title: {title}\n\nCurrent Description: {summary}\n\nSource Context:\n{source_context}",
        )
        user_prompt = user_template.format(title=title, summary=summary, source_context=source_context)

        payload: dict[str, Any] = {
            "model": self._request_model_name(model),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.1,
            "response_format": schema,
        }

        started = time.perf_counter()
        response = self._post("chat/completions", payload)
        latency_ms = int((time.perf_counter() - started) * 1000)
        response.raise_for_status()
        data: dict[str, Any] = response.json()
        choices = data.get("choices")
        first_choice: dict[str, Any] = {}
        if isinstance(choices, list) and choices and isinstance(choices[0], dict):
            first_choice = cast(dict[str, Any], choices[0])
        message = first_choice.get("message", {})
        message_map: dict[str, Any] = cast(dict[str, Any], message) if isinstance(message, dict) else {}
        content = str(message_map.get("content", "{}") or "{}").strip()
        parsed: dict[str, Any] = json.loads(content)
        return {
            "title": str(parsed.get("title") or title).strip(),
            "description": str(parsed.get("description") or summary).strip(),
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
            "model": self._request_model_name(model),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.0,
            "response_format": schema,
        }

        started = time.perf_counter()
        response = self._post("chat/completions", payload)
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
            "model": self._request_model_name(model),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.0,
            "response_format": schema,
        }

        started = time.perf_counter()
        response = self._post("chat/completions", payload)
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

        business_impact = str(parsed.get("business_impact") or "").strip()
        if business_impact not in BUSINESS_IMPACT_TAGS.values():
            business_impact = BUSINESS_IMPACT_TAGS.get(business_level_int, "")
        technical_impact = str(parsed.get("technical_impact") or "").strip()
        if technical_impact not in TECHNICAL_IMPACT_TAGS.values():
            technical_impact = TECHNICAL_IMPACT_TAGS.get(technical_level_int, "")

        return {
            "business_level": business_level,
            "technical_level": technical_level,
            "business_impact": business_impact,
            "technical_impact": technical_impact,
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


class OpenAIAPIClient(GitHubModelsClient):
    def __init__(
        self,
        *,
        api_key: str | None = None,
        token_provider: OpenAIWorkloadIdentityTokenProvider | None = None,
        endpoint: str = "https://api.openai.com/v1",
        timeout_sec: int = 25,
    ):
        if not api_key and token_provider is None:
            raise LLMProviderConfigError("OpenAI API client requires OPENAI_API_KEY or workload identity settings")
        self.api_key = api_key
        self.token_provider = token_provider
        super().__init__(token=api_key or "", endpoint=endpoint, timeout_sec=timeout_sec)

    @classmethod
    def from_env(
        cls,
        environ: dict[str, str] | None = None,
        *,
        endpoint: str | None = None,
        timeout_sec: int = 25,
    ) -> "OpenAIAPIClient":
        env = environ or os.environ
        api_key = env.get("OPENAI_API_KEY", "").strip()
        base_url = (endpoint or env.get("OPENAI_BASE_URL", "") or "https://api.openai.com/v1").strip()
        if not base_url:
            base_url = "https://api.openai.com/v1"
        if api_key:
            return cls(api_key=api_key, endpoint=base_url, timeout_sec=timeout_sec)
        token_provider = OpenAIWorkloadIdentityTokenProvider.from_env(env, timeout_sec=timeout_sec)
        return cls(token_provider=token_provider, endpoint=base_url, timeout_sec=timeout_sec)

    def _request_model_name(self, model: str) -> str:
        normalized = str(model or "").strip()
        if normalized.startswith("openai/"):
            return normalized.split("/", 1)[1]
        return normalized

    def _access_token(self) -> str:
        if self.api_key:
            return self.api_key
        if self.token_provider is None:
            raise LLMProviderConfigError("OpenAI workload identity token provider is not configured")
        return self.token_provider.get_token()

    def _post(self, path: str, payload: dict[str, Any]):
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self._access_token()}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )
        return self.session.post(f"{self.endpoint}/{path.lstrip('/')}", json=payload, timeout=self.timeout_sec)
