from .protocols import Sender
from .request import Request
from .response import Response


class CustomQuerySender:
    def __init__(self, custom_queries: dict[str, str] | None, inner: Sender) -> None:
        self.custom_queries = custom_queries
        self.inner = inner

    def send(self, request: Request) -> Response:
        if self.custom_queries is not None:
            for key, value in self.custom_queries.items():
                request.parameters[key] = value
        return self.inner.send(request)