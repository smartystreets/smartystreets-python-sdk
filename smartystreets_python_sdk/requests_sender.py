from requests import Session, Request
from response import Response
from version import Version


class RequestsSender:
    def __init__(self, max_timeout=10000):
        self.session = Session()
        self.max_timeout = max_timeout

    def send(self, smartyrequest):
        request = self.build_request(smartyrequest)

        response = self.session.send(request, timeout=self.max_timeout)

        return self.build_smartyresponse(response)

    def build_request(self, smartyrequest):
        request = Request(url=smartyrequest.urlprefix, params=smartyrequest.parameters)
        request.headers['User-Agent'] = "smartystreets (sdk:python@" + Version.CURRENT + ")"
        if smartyrequest.referer is not None:
            request.headers['Referer'] = smartyrequest.referer
        request.data = smartyrequest.payload
        request.method = "GET" if smartyrequest.payload is None else "POST"
        prepped_request = self.session.prepare_request(request)
        return prepped_request

    def build_smartyresponse(self, inner_response):
        return Response(inner_response.content, inner_response.status_code)
