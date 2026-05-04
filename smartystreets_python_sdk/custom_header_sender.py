class CustomHeaderSender:
    def __init__(self, headers, inner, append_headers=None):
        self.headers = headers
        self.inner = inner
        self.append_headers = append_headers or {}

    def send(self, request):
        for key, value in self.apply_headers().items():
            request.headers[key] = value
        return self.inner.send(request)

    def apply_headers(self):
        result = {}
        for key, value in self.headers.items():
            if key in self.append_headers:
                separator = self.append_headers[key]
                if isinstance(value, list):
                    result[key] = separator.join(value)
                else:
                    result[key] = value
            else:
                result[key] = value
        return result
