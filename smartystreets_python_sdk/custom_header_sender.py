from typing import Any

from .protocols import Sender
from .request import Request
from .response import Response


class CustomHeaderSender:
    def __init__(self, headers: dict[str, Any], inner: Sender, append_headers: dict[str, str] | None = None) -> None:
        self.headers = headers
        self.inner = inner
        self.append_headers = append_headers or {}

    def send(self, request: Request) -> Response:
        for key, value in self.apply_headers().items():
            request.headers[key] = value
        return self.inner.send(request)

    def apply_headers(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in self.headers.items():
            if key in self.append_headers:
                separator = self.append_headers[key]
                if isinstance(value, list):
                    result[key] = separator.join(value)
                else:
                    result[key] = value
            else:
                result[key] = value
        return result
