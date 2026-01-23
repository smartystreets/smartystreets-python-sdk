class CredentialsRequired(Exception):
    pass


class BasicAuthCredentials:
    def __init__(self, auth_id, auth_token):
        if not auth_id or not auth_token:
            raise CredentialsRequired("credentials (auth_id, auth_token) required")
        self.auth_id = auth_id
        self.auth_token = auth_token

    def sign(self, request):
        request.auth = (self.auth_id, self.auth_token)
