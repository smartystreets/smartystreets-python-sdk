from requests import Session, Request
from response import Response
from version import Version


class RequestsSender:
    def __init__(self, max_timeout=10000):
        self.session = Session()
        self.max_timeout = max_timeout

    def send(self, smarty_request):
        request = self.build_request(smarty_request)
        prepped_request = self.session.prepare_request(request)

        response = self.session.send(prepped_request, timeout=self.max_timeout)

        return self.build_smarty_response(response)

    def build_request(self, smarty_request):
        request = Request(url=smarty_request.urlprefix, params=smarty_request.parameters)
        request.headers['User-Agent'] = "smartystreets (sdk:python@" + Version.CURRENT + ")"
        if smarty_request.referer is not None:
            request.headers['Referer'] = smarty_request.referer
        request.data = smarty_request.payload
        request.method = "GET" if smarty_request.payload is None else "POST"
        return request

    def build_smarty_response(self, inner_response):
        return Response(inner_response.content, inner_response.status_code)
