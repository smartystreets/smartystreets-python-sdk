import unittest

from smartystreets_python_sdk import Response, errors, exceptions
from smartystreets_python_sdk.exceptions import BadRequestError
from smartystreets_python_sdk.status_code_sender import StatusCodeSender
from test.mocks import MockSender


class TestStatusCodeSender(unittest.TestCase):
    def test_not_modified_is_not_an_error(self):
        inner = MockSender(Response("", 304, {'Etag': 'server-refreshed-etag'}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsNone(response.error)
        self.assertEqual(304, response.status_code)
        self.assertEqual('server-refreshed-etag', response.find_header('etag'))

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
        self.assertEqual(errors.BAD_REQUEST + " Body:", str(response.error))

    def test_each_status_code_uses_api_message_when_present(self):
        payload = '{"errors": [{"message": "API says no"}]}'
        expected_types = {400: exceptions.BadRequestError,
                          401: exceptions.BadCredentialsError,
                          402: exceptions.PaymentRequiredError,
                          403: exceptions.ForbiddenError,
                          408: exceptions.RequestTimeoutError,
                          413: exceptions.RequestEntityTooLargeError,
                          422: exceptions.UnprocessableEntityError,
                          429: exceptions.TooManyRequestsError,
                          500: exceptions.InternalServerError,
                          502: exceptions.BadGatewayError,
                          503: exceptions.ServiceUnavailableError,
                          504: exceptions.GatewayTimeoutError}

        for status_code, error_type in expected_types.items():
            with self.subTest(status_code=status_code):
                inner = MockSender(Response(payload, status_code, {}))

                response = StatusCodeSender(inner).send(None)

                self.assertIsInstance(response.error, error_type)
                self.assertEqual('API says no', str(response.error))

    def test_each_status_code_falls_back_to_standard_message(self):
        expected_messages = {400: errors.BAD_REQUEST,
                             401: errors.BAD_CREDENTIALS,
                             402: errors.PAYMENT_REQUIRED,
                             403: errors.FORBIDDEN,
                             408: errors.REQUEST_TIMEOUT,
                             413: errors.REQUEST_ENTITY_TOO_LARGE,
                             422: errors.UNPROCESSABLE_ENTITY,
                             429: errors.TOO_MANY_REQUESTS,
                             500: errors.INTERNAL_SERVER_ERROR,
                             502: errors.BAD_GATEWAY,
                             503: errors.SERVICE_UNAVAILABLE,
                             504: errors.GATEWAY_TIMEOUT}

        for status_code, message in expected_messages.items():
            with self.subTest(status_code=status_code):
                inner = MockSender(Response("", status_code, {}))

                response = StatusCodeSender(inner).send(None)

                self.assertEqual(message + " Body:", str(response.error))

    def test_standard_messages_match_shared_wording(self):
        self.assertEqual("Bad Request (Malformed Payload): A GET request lacked a required field or the"
                         " request body of a POST request contained malformed JSON.", errors.BAD_REQUEST)
        self.assertEqual("Forbidden: The request contained valid data and was understood by the server,"
                         " but the server is refusing action.", errors.FORBIDDEN)
        self.assertEqual("Request timeout error.", errors.REQUEST_TIMEOUT)
        self.assertEqual("Too Many Requests: The rate limit for your account has been exceeded.",
                         errors.TOO_MANY_REQUESTS)
        self.assertEqual("Bad Gateway error.", errors.BAD_GATEWAY)

    def test_unexpected_status_code_falls_back_to_standard_message(self):
        inner = MockSender(Response("", 418, {}))

        response = StatusCodeSender(inner).send(None)

        self.assertIsInstance(response.error, exceptions.SmartyException)
        self.assertEqual('The server returned an unexpected HTTP status code: 418 Body:', str(response.error))

    def test_unexpected_status_code_uses_api_message_when_present(self):
        payload = '{"errors": [{"message": "API teapot message"}]}'
        inner = MockSender(Response(payload, 418, {}))

        response = StatusCodeSender(inner).send(None)

        self.assertIsInstance(response.error, exceptions.SmartyException)
        self.assertEqual('API teapot message', str(response.error))

    def test_fallback_appends_unparseable_body(self):
        inner = MockSender(Response("not json", 400, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertIsInstance(response.error, BadRequestError)
        self.assertEqual(errors.BAD_REQUEST + " Body: not json", str(response.error))

    def test_fallback_appends_body_without_messages(self):
        inner = MockSender(Response('{"errors": []}', 422, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertEqual(errors.UNPROCESSABLE_ENTITY + ' Body: {"errors": []}', str(response.error))

    def test_blank_body_yields_empty_body_label(self):
        inner = MockSender(Response("   ", 422, {}))
        sender = StatusCodeSender(inner)

        response = sender.send(None)

        self.assertEqual(errors.UNPROCESSABLE_ENTITY + " Body:", str(response.error))


if __name__ == '__main__':
    unittest.main()
