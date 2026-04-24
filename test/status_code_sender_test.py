import unittest

from smartystreets_python_sdk import Response
from smartystreets_python_sdk.exceptions import NotModifiedError
from smartystreets_python_sdk.status_code_sender import StatusCodeSender
from test.mocks import MockSender


class TestStatusCodeSender(unittest.TestCase):
    def test_not_modified_error_carries_response_etag(self):
        inner = MockSender(Response("", 304, {'Etag': 'server-refreshed-etag'}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsInstance(response.error, NotModifiedError)
        self.assertEqual('server-refreshed-etag', response.error.response_etag)

    def test_not_modified_error_response_etag_is_case_insensitive(self):
        inner = MockSender(Response("", 304, {'eTaG': 'case-insensitive-etag'}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsInstance(response.error, NotModifiedError)
        self.assertEqual('case-insensitive-etag', response.error.response_etag)

    def test_not_modified_error_response_etag_none_when_header_absent(self):
        inner = MockSender(Response("", 304, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsInstance(response.error, NotModifiedError)
        self.assertIsNone(response.error.response_etag)

    def test_ok_status_has_no_error(self):
        inner = MockSender(Response("", 200, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsNone(response.error)


if __name__ == '__main__':
    unittest.main()
