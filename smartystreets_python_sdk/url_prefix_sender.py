class URLPrefixSender:
    def __init__(self, url_prefix, inner):
        self.url_prefix = url_prefix
        self.inner = inner

    def send(self, request):
        if request.url_prefix is not None:
            request.url_prefix = self.url_prefix + request.url_prefix
        else:
            request.url_prefix = self.url_prefix

        return self.inner.send(request)
