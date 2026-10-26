from typing import Any, Protocol

from .request import Request
from .response import Response


class Sender(Protocol):
    def send(self, request: Request) -> Response: ...


class Serializer(Protocol):
    def serialize(self, obj: Any) -> bytes: ...

    def deserialize(self, payload: Any) -> Any: ...


class Signer(Protocol):
    def sign(self, request: Request) -> None: ...
