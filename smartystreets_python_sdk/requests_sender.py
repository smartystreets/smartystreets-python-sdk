from requests import Session, Request
from .response import Response
import smartystreets_python_sdk as smarty


class RequestsSender:
    def __init__(self, max_timeout=10000):
        self.session = Session()
        self.max_timeout = max_timeout

    def send(self, smarty_request):
        request = build_request(smarty_request)
        prepped_request = self.session.prepare_request(request)

        try:
            response = self.session.send(prepped_request, timeout=self.max_timeout)
        except Exception as e:
            return Response(None, None, e)

        return build_smarty_response(response)


def build_request(smarty_request):
    request = Request(url=smarty_request.url_prefix, params=smarty_request.parameters)
    request.headers['User-Agent'] = "smartystreets (sdk:python@{})".format(smarty.__version__)
    if smarty_request.referer is not None:
        request.headers['Referer'] = smarty_request.referer
    request.data = smarty_request.payload
    request.method = "POST"
    return request


def build_smarty_response(inner_response):
    return Response(inner_response.text, inner_response.status_code)
