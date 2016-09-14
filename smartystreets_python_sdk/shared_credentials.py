class SharedCredentials:
    def __init__(self, id, host_name):
        self.id = id
        self.host_name = host_name

    def sign(self, request):
        request.parameters['auth-id'] = self.id
        request.referer = "https://" + self.host_name
