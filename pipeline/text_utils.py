import hashlib
import re
import unicodedata
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

TRACKING_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "utm_id",
    "gclid",
    "fbclid",
    "mc_cid",
    "mc_eid",
}


def normalize_text(value: str) -> str:
    if not value:
        return ""
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url.strip())
    query = [(k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True) if k.lower() not in TRACKING_PARAMS]
    canonical = parsed._replace(query=urlencode(query), fragment="")
    return urlunparse(canonical)


def story_fingerprint(title: str, domain: str, day_bucket: str) -> str:
    base = f"{normalize_text(title).lower()}|{domain.lower()}|{day_bucket}"
    return hashlib.sha1(base.encode("utf-8")).hexdigest()


def stable_id(prefix: str, value: str) -> str:
    return f"{prefix}_{hashlib.sha1(value.encode('utf-8')).hexdigest()[:16]}"


def parse_datetime(value: str):
    if not value:
        return None
    raw = value.strip()
    if not raw:
        return None
    if raw.endswith("Z"):
        raw = raw.replace("Z", "+00:00")
    for parser in (
        datetime.fromisoformat,
    ):
        try:
            dt = parser(raw)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            continue
    return None


def to_iso(dt: datetime | None, default_now: bool = False) -> str:
    if dt is None and default_now:
        dt = datetime.now(timezone.utc)
    if dt is None:
        return ""
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
