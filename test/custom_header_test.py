from smartystreets_python_sdk.custom_header_sender import CustomHeaderSender
import smartystreets_python_sdk as smarty
import unittest
from mock import patch


def mocked_session_send(request, **kwargs):
    class MockResponse:
        def __init__(self, payload, status_code):
            self.text = payload
            self.status_code = status_code

        def json(self):
            return self.text

    if request.url == 'http://localhost/error':
        mockresponse = MockResponse("Error test", 400)
    else:
        mockresponse = MockResponse("This is the test payload.", 200)

    return mockresponse

class TestCustomHeaderSender(unittest.TestCase):
    sender = smarty.