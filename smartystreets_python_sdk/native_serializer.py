import json
from typing import Any


class NativeSerializer:
    def __init__(self) -> None:
        pass

    def serialize(self, obj: Any) -> bytes:
        return json.dumps(obj).encode("UTF-8")

    def deserialize(self, payload: Any) -> Any:
        if not payload:
            return {}
        return json.loads(payload)
