from requests import Request


class CustomHeaderSender:
    def __init__(self, headers, inner, append_headers=None):
        self.headers = headers
        self.inner = inner
        self.append_headers = append_headers or {}

    def send(self, smarty_request):
        request = self.build_request(smarty_request)
        return self.inner.send(request)

    def build_request(self, smarty_request):
        request = Request(url=smarty_request.url_prefix, params=smarty_request.parameters)
        request.headers = self.apply_headers()
        if smarty_request.payload:
            request.data = smarty_request.payload
            request.method = 'POST'
        else:
            request.method = 'GET'
        return request

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
