import smartystreets_python_sdk as smarty
import unittest
from test.mocks import RequestCapturingSender


class TestXForwardedFor(unittest.TestCase):

    def test_x_forwarded_for_header_set_via_client_builder(self):
        capturing_sender = RequestCapturingSender()
        credentials = smarty.StaticCredentials("test-id", "test-token")
        client = smarty.ClientBuilder(credentials) \
            .with_x_forwarded_for('0.0.0.0') \
            .with_sender(capturing_sender) \
            .build_us_street_api_client()

        from smartystreets_python_sdk.us_street import Lookup
        lookup = Lookup()
        lookup.street = "1 Rosedale"
        client.send_lookup(lookup)

        self.assertEqual('0.0.0.0', capturing_sender.request.headers['X-Forwarded-For'])

    def test_x_forwarded_for_combined_with_custom_headers(self):
        capturing_sender = RequestCapturingSender()
        credentials = smarty.StaticCredentials("test-id", "test-token")
        client = smarty.ClientBuilder(credentials) \
            .with_x_forwarded_for('0.0.0.0') \
            .with_custom_header({'X-Custom': 'value'}) \
            .with_sender(capturing_sender) \
            .build_us_street_api_client()

        from smartystreets_python_sdk.us_street import Lookup
        lookup = Lookup()
        lookup.street = "1 Rosedale"
        client.send_lookup(lookup)

        self.assertEqual('0.0.0.0', capturing_sender.request.headers['X-Forwarded-For'])
        self.assertEqual('value', capturing_sender.request.headers['X-Custom'])
