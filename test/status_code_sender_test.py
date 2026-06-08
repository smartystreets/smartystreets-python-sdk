import unittest

from smartystreets_python_sdk import Response, errors
from smartystreets_python_sdk.exceptions import BadRequestError, NotModifiedError
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

    def test_client_error_uses_message_from_response(self):
        payload = '{"errors": [{"message": "Invalid postal code."}]}'
        inner = MockSender(Response(payload, 400, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsInstance(response.error, BadRequestError)
        self.assertEqual('Invalid postal code.', str(response.error))

    def test_client_error_joins_multiple_messages(self):
        payload = '{"errors": [{"message": "First problem."}, {"message": "Second problem."}]}'
        inner = MockSender(Response(payload, 422, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertEqual('First problem. Second problem.', str(response.error))

    def test_client_error_falls_back_when_no_message(self):
        inner = MockSender(Response("", 400, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsInstance(response.error, BadRequestError)
        self.assertEqual(errors.BAD_REQUEST, str(response.error))


if __name__ == '__main__':
    unittest.main()
