class LicenseSender:
    def __init__(self, licenses, inner):
        self.licenses = licenses
        self.inner = inner

    def send(self, request):
        if len(self.licenses) > 0:
            request.parameters["license"] = ','.join(self.licenses)
        return self.inner.send(request)
