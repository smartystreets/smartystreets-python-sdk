from .protocols import Sender
from .request import Request
from .response import Response


class URLPrefixSender:
    def __init__(self, url_prefix: str, inner: Sender) -> None:
        self.url_prefix = url_prefix
        self.inner = inner

    def send(self, request: Request) -> Response:
        if request.url_components:
            request.url_prefix = self.url_prefix + request.url_components
        else:
            request.url_prefix = self.url_prefix
        return self.inner.send(request)
