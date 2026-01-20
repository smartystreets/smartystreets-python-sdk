from smartystreets_python_sdk.exceptions import SmartyException


class BasicAuthCredentials:
    def __init__(self, auth_id, auth_token):
        if not auth_id or not auth_token:
            raise SmartyException('credentials (auth id, auth token) required')
        self.auth_id = auth_id
        self.auth_token = auth_token

    def sign(self, request):
        request.basic_auth = (self.auth_id, self.auth_token)
