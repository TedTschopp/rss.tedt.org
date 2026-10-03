"""Recover GAI briefing selections with explicit sources and estimated ratings."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import logging
import math
from pathlib import Path
import re
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup
import requests

BRIEFING_URL = "https://gaiinsights.com/articles"
BRIEFINGS_PATH = Path("derived/gai_briefings.json")
REPORT_PATH = Path("reports/gai_recovery_report.json")
RATINGS = {"Essential", "Important", "Optional"}
logger = logging.getLogger(__name__)


def canonical_url(url: str) -> str:
    """Remove marketing parameters while retaining article identifiers."""
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        return ""
    tracking = {"_gl", "_ga", "_gcl_au", "hss_channel", "hsenc", "hsmi", "mod", "ab", "deliveryName"}
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if not k.lower().startswith("utm_") and k not in tracking]
    host = parts.netloc.lower().removeprefix("www.")
    return urlunsplit(("https", host, parts.path.rstrip("/"), urlencode(sorted(query)), ""))


def row_date(row: dict):
    text = row.get("Date", {}).get("text", "")
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except (ValueError, TypeError):
            pass
    return None


def row_url(row: dict) -> str:
    links = row.get("Title", {}).get("links", [])
    return canonical_url(links[0]) if links else ""


def published_rating(row: dict) -> bool:
    cell = row.get("Rating", {})
    # Preserve specialty qualifications such as "Optional, Essential for Bioscience".
    return cell.get("text", "").split(",", 1)[0].strip() in RATINGS and not cell.get("estimated", False)


def title_key(title: str) -> str:
    # Match publisher/archive URLs with the original link using the dated title.
    return " ".join(re.findall(r"\w+", title.casefold()))


def parse_briefing(html: str, *, source_url=BRIEFING_URL, capture_url="",
                   capture_timestamp="", rated_rows=(), now=None) -> dict:
    """Read only the dated briefing section, excluding navigation and promotions.

    An archive timestamp is never substituted for a briefing publication date.
    Older undated pages can use a date only when their published ratings agree.
    """
    soup = BeautifulSoup(html, "html.parser")
    heading = next((h for h in soup.find_all(["h1", "h2"])
                    if re.search(r"In Today.s News Briefing", h.get_text(" ", strip=True))), None)
    if heading is None:
        raise ValueError("GAI briefing heading not found")
    section = heading.find_parent(class_="hhs-rich-text") or heading.parent
    table = section.find("table")
    if table is None:
        raise ValueError("GAI briefing article table not found")
    items = []
    seen = set()
    for anchor in table.find_all("a", href=True):
        href = anchor["href"].strip()
        if href.startswith("#"):
            continue
        url = urljoin(source_url, href)
        key = canonical_url(url)
        title = anchor.get_text(" ", strip=True)
        if key and title and key not in seen:
            items.append({"title": title, "url": url})
            seen.add(key)
    if not items:
        raise ValueError("GAI briefing has no usable article links")

    heading_text = heading.get_text(" ", strip=True)
    date_text = re.sub(r"^.*?News Briefing\s*[-–—:]?\s*", "", heading_text).strip()
    briefing_date = None
    date_basis = "page heading"
    for fmt in ("%B %d, %Y", "%d %B %Y", "%b %d, %Y", "%m/%d/%Y", "%Y-%m-%d"):
        try:
            briefing_date = datetime.strptime(date_text, fmt).date()
            break
        except ValueError:
            pass
    if briefing_date is None:
        # Resolve each link from the publisher's ratings, then require one date
        # shared by every resolvable item. Ambiguous captures stay unimported.
        known = defaultdict(set)
        for row in rated_rows:
            day = row_date(row)
            if published_rating(row) and day and row_url(row):
                known[row_url(row)].add(day)
        matches = [known[canonical_url(item["url"])] for item in items
                   if canonical_url(item["url"]) in known]
        common = set.intersection(*matches) if matches else set()
        if len(common) != 1 or len(matches) < max(2, len(items) - 1):
            raise ValueError("GAI briefing date unavailable; capture date is not a publication date")
        briefing_date = common.pop()
        date_basis = "matching published GAI rating dates"
    current = (now or datetime.now(timezone.utc)).date()
    if briefing_date > current:
        raise ValueError("GAI briefing date is in the future")
    return {
        "date": briefing_date.isoformat(), "date_basis": date_basis,
        "source_url": source_url, "capture_url": capture_url,
        "capture_timestamp": capture_timestamp,
        "source_sha256": hashlib.sha256(html.encode("utf-8")).hexdigest(),
        "items": items,
    }


def load_briefings(path=BRIEFINGS_PATH) -> dict:
    if not Path(path).exists():
        return {"schema_version": 1, "briefings": [], "rating_overrides": {}}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("briefings"), list):
        raise ValueError("Unsupported GAI briefing history")
    return data


def add_briefing(data: dict, briefing: dict) -> bool:
    """Retain changed selections; identical page versions do not grow history."""
    def key(value):
        return (value["date"], tuple(sorted((canonical_url(i["url"]), i["title"])
                                            for i in value["items"])))
    if any(key(old) == key(briefing) for old in data["briefings"]):
        return False
    data["briefings"].append(briefing)
    data["briefings"].sort(key=lambda b: b["date"])
    return True


def save_briefings(data: dict, path=BRIEFINGS_PATH):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


_STOP = set("a an and are as at be been but by can for from has have how in into is it its more new of on or our that the their this to was we what when why with ai analysts article generative insights news".split())


def _tokens(text):
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2 and t not in _STOP]


class HistoricalRatingEstimator:
    """A transparent nearest-example estimate using published GAI ratings only."""

    def __init__(self, rows):
        self.examples = [r for r in rows if published_rating(r)]
        self.counts = [Counter(_tokens(r["Title"]["text"]) * 3 +
                               _tokens(r.get("Rationale", {}).get("text", "")))
                       for r in self.examples]
        frequency = Counter(t for c in self.counts for t in c)
        self.idf = {t: math.log((1 + len(self.counts)) / (1 + n)) + 1
                    for t, n in frequency.items()}
        self.vectors = []
        for count in self.counts:
            vector = {t: (1 + math.log(n)) * self.idf[t] for t, n in count.items()}
            norm = math.sqrt(sum(v * v for v in vector.values())) or 1
            self.vectors.append({t: v / norm for t, v in vector.items()})

    def estimate(self, title: str) -> dict:
        counts = Counter(_tokens(title))
        vector = {t: (1 + math.log(n)) * self.idf[t] for t, n in counts.items() if t in self.idf}
        norm = math.sqrt(sum(v * v for v in vector.values())) or 1
        vector = {t: v / norm for t, v in vector.items()}
        similarities = sorted(((sum(v * other.get(t, 0) for t, v in vector.items()), i)
                               for i, other in enumerate(self.vectors)), reverse=True)[:5]
        votes = defaultdict(float)
        examples = []
        for similarity, index in similarities:
            if similarity < 0.1:
                continue
            row = self.examples[index]
            rating = row["Rating"]["text"].split(",", 1)[0].strip()
            votes[rating] += similarity ** 2
            examples.append({"date": row["Date"]["text"], "title": row["Title"]["text"],
                             "url": row["Title"]["links"][0] if row["Title"]["links"] else "",
                             "rating": rating, "similarity": round(similarity, 4)})
        rating = max(votes, key=votes.get) if votes else "Important"
        return {"rating": rating, "method": "historical nearest examples",
                "confidence": "limited" if not examples or examples[0]["similarity"] < 0.3 else "moderate",
                "rationale": "Estimated from similar historically rated GAI selections." if examples else
                             "Estimated Important as a selected GAI briefing story; close historical examples were unavailable.",
                "examples": examples}


def briefing_rows(data: dict, rated_rows) -> list[dict]:
    estimator = HistoricalRatingEstimator(rated_rows)
    known = {(row_date(r), row_url(r)) for r in rated_rows if published_rating(r)}
    known_titles = {(row_date(r), title_key(r["Title"]["text"])) for r in rated_rows
                    if published_rating(r)}
    overrides = data.get("rating_overrides", {})
    rows = []
    for briefing in data["briefings"]:
        day = datetime.strptime(briefing["date"], "%Y-%m-%d").date()
        for item in briefing["items"]:
            key = canonical_url(item["url"])
            if (day, key) in known or (day, title_key(item["title"])) in known_titles:
                continue
            estimate = overrides.get(key) or estimator.estimate(item["title"])
            if estimate.get("rating") not in RATINGS:
                raise ValueError("Estimated GAI rating must be Essential, Important, or Optional")
            description = (f"Estimated GAI-style rating: {estimate['rating']}. "
                           f"Rationale (estimate): {estimate['rationale']} "
                           f"Selected in GAI Insights' briefing dated {briefing['date']}. "
                           f"Briefing source: {BRIEFING_URL}.")
            if briefing.get("capture_url"):
                description += f" Historical capture: {briefing['capture_url']}."
            rows.append({
                "Date": {"text": day.strftime("%m/%d/%Y"), "links": []},
                "Rating": {"text": estimate["rating"], "links": [], "estimated": True,
                           "method": estimate["method"], "confidence": estimate["confidence"],
                           "examples": estimate.get("examples", [])},
                "Title": {"text": item["title"], "links": [item["url"]]},
                "Rationale": {"text": description, "links": []},
            })
    return rows


def merge_rows(*groups) -> list[dict]:
    """Preserve prior entries and prefer publisher ratings over estimates."""
    merged = {}
    published_keys = set()
    published_titles = set()
    for rows in groups:
        for row in rows:
            day = row_date(row)
            url = row_url(row)
            title = row.get("Title", {}).get("text", "").strip()
            if not day or not title:
                continue
            # Some historical publisher rows reuse a link for different stories.
            # Do not discard those distinct headlines while removing duplicates.
            core = (day, url, title_key(title))
            if published_rating(row):
                published_keys.add(core)
                published_titles.add((day, title_key(title)))
                # Preserve conflicting publisher versions as separate originals.
                # Exact repeated rows share a GUID and need only one feed entry.
                key = (core, row['Rating']['text'], row.get('Rationale', {}).get('text', ''))
            else:
                key = (core, 'estimated')
            merged[key] = row
    rows = [row for key, row in merged.items() if published_rating(row) or
            (key[0] not in published_keys and (key[0][0], key[0][2]) not in published_titles)]
    return sorted(rows, key=lambda r: (row_date(r), row_url(r)), reverse=True)


def supplement_rows(rated_rows, previous_rows=(), *, path=BRIEFINGS_PATH, now=None,
                    ratings_error=None, report_path=REPORT_PATH):
    data = load_briefings(path)
    error = None
    try:
        response = requests.get(BRIEFING_URL, timeout=25)
        response.raise_for_status()
        briefing = parse_briefing(response.content.decode("utf-8", errors="replace"),
                                  rated_rows=rated_rows, now=now)
        if add_briefing(data, briefing):
            save_briefings(data, path)
    except (requests.RequestException, ValueError) as exc:
        error = str(exc)
        logger.warning("GAI briefing lookup unavailable: %s", error)
    baseline = merge_rows(previous_rows, rated_rows)
    recovered = briefing_rows(data, baseline)
    merged = merge_rows(baseline, recovered)
    current = (now or datetime.now(timezone.utc)).date()
    latest_rated = max((row_date(r) for r in merged if published_rating(r)), default=None)
    latest = max((row_date(r) for r in merged), default=None)
    report = {
        "timestamp": (now or datetime.now(timezone.utc)).isoformat(),
        "status": "supplemented" if latest and (not latest_rated or latest > latest_rated) else "ratings",
        "ratings_url": "https://gaiinsights.com/ratings", "briefing_url": BRIEFING_URL,
        "latest_published_rating_date": str(latest_rated) if latest_rated else None,
        "latest_selection_date": str(latest) if latest else None,
        "ratings_age_days": (current - latest_rated).days if latest_rated else None,
        "total_rows": len(merged), "published_ratings": sum(published_rating(r) for r in merged),
        "estimated_ratings": sum(bool(r["Rating"].get("estimated")) for r in merged),
        "briefing_versions": len(data["briefings"]), "briefing_lookup_error": error,
        "ratings_lookup_error": ratings_error, "fetched_rating_rows": len(rated_rows),
        "archive_recovery": data.get("archive_recovery", {}),
    }
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return merged
