import base64
import struct
from typing import Any


EMBEDDING_PREFIX = "f32:"


def encode_embedding(vector: list[Any]) -> str:
    values = [float(value) for value in vector]
    if not values:
        return EMBEDDING_PREFIX
    packed = struct.pack(f"<{len(values)}f", *values)
    return EMBEDDING_PREFIX + base64.b64encode(packed).decode("ascii")


def decode_embedding(value: Any) -> list[float]:
    if isinstance(value, list):
        try:
            return [float(item) for item in value]
        except (TypeError, ValueError):
            return []
    if not isinstance(value, str) or not value.startswith(EMBEDDING_PREFIX):
        return []
    try:
        packed = base64.b64decode(value[len(EMBEDDING_PREFIX) :], validate=True)
        if len(packed) % 4:
            return []
        count = len(packed) // 4
        return list(struct.unpack(f"<{count}f", packed)) if count else []
    except (ValueError, struct.error):
        return []
