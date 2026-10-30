from typing import Any, Mapping


class Response:
    def __init__(self, payload: Any, status_code: int, headers: Mapping[str, Any] | None = None,
                 error: Exception | None = None) -> None:
        self.payload = payload
        self.status_code = status_code
        self.headers = headers
        self.error = error

    def getHeader(self, header: str) -> Any:
        if self.headers is None:
            return None
        else:
            return self.headers[header]

    def find_header(self, name: str) -> Any:
        if self.headers is None:
            return None
        target = name.lower()
        for key, value in self.headers.items():
            if key.lower() == target:
                return value
        return None
