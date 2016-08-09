from requests import Session, Request
from response import Response
from version import Version


class RequestsSender:
    def __init__(self, maxtimeout=10000):
        self.session = Session()
        self.maxtimeout = maxtimeout

    def send(self, smartyrequest):
        request = self.build_request(smartyrequest)

        response = self.session.send(request, timeout=self.maxtimeout)

        return self.build_smartyresponse(response)

    def build_request(self, smartyrequest):
        request = Request(url=smartyrequest.urlprefix, params=smartyrequest.parameters)
        request.headers['User-Agent'] = "smartystreets (sdk:python@" + Version.CURRENT + ")"
        request.data = smartyrequest.payload
        request.method = "GET" if smartyrequest.payload is None else "POST"
        preppedrequest = self.session.prepare_request(request)
        return preppedrequest

    def build_smartyresponse(self, response):
        return Response(response.payload, response.status_code)
