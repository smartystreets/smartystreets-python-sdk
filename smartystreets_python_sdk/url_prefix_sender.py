class URLPrefixSender:
    def __init__(self, url_prefix, inner):
        self.url_prefix = url_prefix
        self.inner = inner

    def send(self, request):
        if request.url_components:
            request.url_prefix = self.url_prefix + request.url_components
        else:
            request.url_prefix = self.url_prefix
        return self.inner.send(request)
