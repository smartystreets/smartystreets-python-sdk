class CustomHeaderSender:
    def __init__(self, headers, inner):
        self.headers = headers
        self.inner = inner

    def send(self, request):
        request.headers = self.headers
        return self.inner.send(request)
