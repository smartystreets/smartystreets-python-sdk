from .request import Request


class SharedCredentials:
    def __init__(self, id: str, host_name: str) -> None:
        self.id = id
        self.host_name = host_name

    def sign(self, request: Request) -> None:
        request.parameters['key'] = self.id
        request.referer = "https://" + self.host_name
