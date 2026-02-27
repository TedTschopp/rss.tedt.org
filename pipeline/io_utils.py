import json
from pathlib import Path
from typing import Any, Iterable


def ensure_dirs(paths: Iterable[str]) -> None:
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)


def read_json(path: str, default: Any):
    file_path = Path(path)
    if not file_path.exists():
        return default
    try:
        with file_path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except Exception:
        return default


def write_json(path: str, payload: Any) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)


def append_jsonl(path: str, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
