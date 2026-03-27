import unittest

from smartystreets_python_sdk import ClientBuilder, StaticCredentials
from smartystreets_python_sdk.us_street import Lookup
from test.mocks import RequestCapturingSender


class TestClientBuilder(unittest.TestCase):
    def test_with_sender_wraps_with_middleware_chain(self):
        capturing_sender = RequestCapturingSender()
        credentials = StaticCredentials("test-id", "test-token")
        client = ClientBuilder(credentials) \
            .with_sender(capturing_sender) \
            .build_us_street_api_client()

        lookup = Lookup()
        lookup.street = "1 Rosedale"
        client.send_lookup(lookup)

        self.assertIn("us-street.api.smarty.com", capturing_sender.request.url_prefix)
        self.assertEqual("test-id", capturing_sender.request.parameters["auth-id"])
        self.assertEqual("test-token", capturing_sender.request.parameters["auth-token"])
