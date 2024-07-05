import smartystreets_python_sdk as smarty
import unittest
from mock import patch


def mocked_session_send(request, **kwargs):
    class MockResponse:
        def __init__(self, payload, status_code):
            self.text = payload
            self.status_code = status_code
            self.headers = None

        def __enter__(self):
            return self

        def __exit__(self, type, value, traceback):
            pass

        def json(self):
            return self.text

    mockresponse = MockResponse("This is the test payload.", 200)

    return mockresponse


class TestCustomHeaderSender(unittest.TestCase):

    def test_populates_header(self):
        sender = smarty.RequestsSender(ip = '0.0.0.0')

        self.assertEqual(sender.ip, '0.0.0.0')

    @patch('requests.Session.send', side_effect=mocked_session_send)
    def test_x_forwarded_for_header_set(self, mock_send):
        sender = smarty.RequestsSender(ip = '0.0.0.0')
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        request = smarty.requests_sender.build_request(smartyrequest, '0.0.0.0')

        self.assertEqual('0.0.0.0', request.headers['X-Forwarded-For'])

    @patch('requests.Session.send', side_effect=mocked_session_send)
    def test_custom_headers_used(self, mock_send):
        sender = smarty.RequestsSender(ip = '0.0.0.0')
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        request = smarty.requests_sender.build_request(smartyrequest, '0.0.0.0')

        self.assertEqual('0.0.0.0', request.headers['X-Forwarded-For'])