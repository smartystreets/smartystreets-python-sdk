from collections import OrderedDict
from typing import Any


class Request:
    def __init__(self) -> None:
        self.parameters: dict[str, Any] = OrderedDict()
        self.payload: bytes | str | None = None
        self.url_prefix: str | None = None
        self.url_components: str | None = None
        self.referer: str | None = None
        self.content_type: str = 'application/json'
        self.auth: tuple[str, str] | None = None
        self.headers: dict[str, Any] = {}
