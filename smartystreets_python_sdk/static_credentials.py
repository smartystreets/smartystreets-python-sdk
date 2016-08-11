class StaticCredentials:
    def __init__(self, auth_id, auth_token):
        self.auth_id = auth_id
        self.auth_token = auth_token

    def sign(self, request):
        request.parameters['auth-id'] = self.auth_id
        request.parameters['auth-token'] = self.auth_token
