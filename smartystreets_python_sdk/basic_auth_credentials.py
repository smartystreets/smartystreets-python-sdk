from .request import Request


class CredentialsRequired(Exception):
    pass


class BasicAuthCredentials:
    def __init__(self, auth_id: str, auth_token: str) -> None:
        if not auth_id or not auth_token:
            raise CredentialsRequired("credentials (auth_id, auth_token) required")
        self.auth_id = auth_id
        self.auth_token = auth_token

    def sign(self, request: Request) -> None:
        request.auth = (self.auth_id, self.auth_token)
