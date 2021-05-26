class LicenseSender:
    def __init__(self, licenses, inner):
        self.licenses = licenses
        self.inner = inner

    def send(self, request):
        if len(self.licenses) > 0:
            request.parameters["license"] = ','.join([str(x) for x in self.licenses])
        return self.inner.send(request)
