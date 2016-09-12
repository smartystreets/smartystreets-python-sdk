class URLPrefixSender:
    def __init__(self, url_prefix, inner):
        self.url_prefix = url_prefix
        self.inner = inner

    def send(self, request):
        request.urlprefix = self.url_prefix

        return self.inner.send(request)
