from .protocols import Sender, Signer
from .request import Request
from .response import Response


class SigningSender:
    def __init__(self, signer: Signer, inner: Sender) -> None:
        self.signer = signer
        self.inner = inner

    def send(self, request: Request) -> Response:
        self.signer.sign(request)
        return self.inner.send(request)
