class SigningSender:
    def __init__(self, signer, inner):
        self.signer = signer
        self.inner = inner

    def send(self, request):
        self.signer.sign(request)
        return self.inner.send(request)
