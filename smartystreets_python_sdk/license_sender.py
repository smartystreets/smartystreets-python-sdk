from .protocols import Sender
from .request import Request
from .response import Response


class LicenseSender:
    def __init__(self, licenses: list[str], inner: Sender) -> None:
        self.licenses = licenses
        self.inner = inner

    def send(self, request: Request) -> Response:
        if len(self.licenses) > 0:
            request.parameters["license"] = ','.join([str(x) for x in self.licenses])
        return self.inner.send(request)
