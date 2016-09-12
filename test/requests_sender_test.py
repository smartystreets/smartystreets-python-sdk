import smartystreets_python_sdk as smarty
import unittest
from mock import patch


def mocked_session_send(request, **kwargs):
    class MockResponse:
        def __init__(self, payload, status_code):
            self.payload = payload
            self.status_code = status_code

        def json(self):
            return self.payload

    if request.url == 'http://localhost/error':
        mockresponse = MockResponse("Error test", 400)
    else:
        mockresponse = MockResponse("This is the test payload.", 200)

    return mockresponse


class TestRequestsSender(unittest.TestCase):
    """
    def test_request_contains_correct_headers(self):
        sender = smarty.RequestsSender()
        smartyrequest = smarty.Request("http://localhost")
        smartyrequest.headers['X-name1'] = "value1"
        smartyrequest.headers['X-name2'] = "value2"

        request = sender.build_request(smartyrequest)

        self.assertEqual("value1", request.headers['X-name1'])
        self.assertEqual("value2", request.headers['X-name2'])
    """
    def test_http_request_contains_get_when_appropriate(self):
        sender = smarty.RequestsSender()
        smartyrequest = smarty.Request()
        smartyrequest.urlprefix = "http://localhost"

        request = sender.build_request(smartyrequest)

        self.assertEqual("GET", request.method)

    def test_http_request_contains_post_when_appropriate(self):
        sender = smarty.RequestsSender()
        smartyrequest = smarty.Request()
        smartyrequest.urlprefix = "http://localhost"

        smartyrequest.payload = "Test Payload"
        request = sender.build_request(smartyrequest)

        self.assertEqual("POST", request.method)

    def test_request_contains_correct_content(self):
        sender = smarty.RequestsSender()
        smartyrequest = smarty.Request()
        smartyrequest.urlprefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        request = sender.build_request(smartyrequest)

        self.assertEqual("This is the test content.", request.body)

    @patch('requests.Session.send', side_effect=mocked_session_send)
    def test_smartyresponse_contains_correct_payload(self, mock_send):
        sender = smarty.RequestsSender()
        smartyrequest = smarty.Request()
        smartyrequest.urlprefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        response = sender.send(smartyrequest)

        self.assertEqual("This is the test payload.", response.payload)

    @patch('requests.Session.send', side_effect=mocked_session_send)
    def test_smartyresponse_contains_status_code_200_on_success(self, mock_send):
        sender = smarty.RequestsSender()
        smartyrequest = smarty.Request()
        smartyrequest.urlprefix = "http://localhost"

        response = sender.send(smartyrequest)

        self.assertEqual(200, response.status_code)

    @patch('requests.Session.send', side_effect=mocked_session_send)
    def test_smartyresponse_contains_status_code_400_when_server_gives_a_400(self, mock_send):
        sender = smarty.RequestsSender()
        smartyrequest = smarty.Request()
        smartyrequest.urlprefix = "http://localhost/error"

        response = sender.send(smartyrequest)

        self.assertEqual(400, response.status_code)
