import re
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


DEFAULT_USER_AGENT = "rss.tedt.org-article-fetcher/1.0 (+https://rss.tedt.org)"
DEFAULT_MAX_CHARS = 12000
CONTENT_TAGS = {"h1", "h2", "h3", "h4", "p", "li", "blockquote", "pre"}
REMOVE_TAGS = {"script", "style", "noscript", "svg", "nav", "footer", "header", "aside", "form"}


def _clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def _truncate(value: str, max_chars: int) -> str:
    if max_chars <= 0 or len(value) <= max_chars:
        return value
    return value[:max_chars].rstrip() + "\n\n[truncated]"


def _content_root(soup: BeautifulSoup):
    return (
        soup.find("article")
        or soup.find("main")
        or soup.find(attrs={"role": "main"})
        or soup.body
        or soup
    )


def html_to_markdown(html: str, *, max_chars: int = DEFAULT_MAX_CHARS) -> str:
    soup = BeautifulSoup(html or "", "html.parser")
    for tag in soup.find_all(REMOVE_TAGS):
        tag.decompose()

    root = _content_root(soup)
    lines: list[str] = []
    seen: set[str] = set()

    for element in root.find_all(CONTENT_TAGS):
        text = _clean_text(element.get_text(" ", strip=True))
        if not text or text in seen:
            continue
        seen.add(text)

        tag_name = element.name or ""
        if tag_name in {"h1", "h2", "h3", "h4"}:
            level = min(4, max(1, int(tag_name[1:])))
            lines.append(f"{'#' * level} {text}")
        elif tag_name == "li":
            lines.append(f"- {text}")
        elif tag_name == "blockquote":
            lines.append(f"> {text}")
        else:
            lines.append(text)

    if not lines:
        fallback = _clean_text(root.get_text(" ", strip=True))
        if fallback:
            lines.append(fallback)

    return _truncate("\n\n".join(lines).strip(), max_chars)


def fetch_article_markdown(
    url: str,
    *,
    timeout_sec: int = 15,
    max_chars: int = DEFAULT_MAX_CHARS,
    session: requests.Session | None = None,
    user_agent: str = DEFAULT_USER_AGENT,
) -> str:
    parsed = urlparse(str(url or "").strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return ""

    active_session = session or requests.Session()
    try:
        response = active_session.get(
            str(url).strip(),
            timeout=timeout_sec,
            headers={"User-Agent": user_agent},
        )
        response.raise_for_status()
        content_type = (response.headers.get("content-type") or "").lower()
        if content_type and "html" not in content_type and "text" not in content_type:
            return ""
        return html_to_markdown(response.text, max_chars=max_chars)
    except Exception:
        return ""