import smartystreets_python_sdk as smarty
import unittest
from test.mocks import *


class TestCustomHeaderSender(unittest.TestCase):

    def test_populates_headers(self):
        sender = smarty.CustomHeaderSender(
            {'Test-User-Agent': 'Test-Agent', 'Test-Content-Type': 'Test-Type'},
            MockSender(None)
        )
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"

        sender.send(smartyrequest)

        self.assertEqual('Test-Agent', smartyrequest.headers['Test-User-Agent'])
        self.assertEqual('Test-Type', smartyrequest.headers['Test-Content-Type'])

    def test_multiple_with_custom_header_calls_merge_headers(self):
        builder = smarty.ClientBuilder(None)
        builder.with_custom_header({'User-Agent': 'Test-Agent'})
        builder.with_custom_header({'Content-Type': 'Test-Type'})

        self.assertEqual('Test-Agent', builder.header['User-Agent'])
        self.assertEqual('Test-Type', builder.header['Content-Type'])

    def test_send_forwards_smarty_request_with_upstream_state_intact(self):
        inner = MockSender(None)
        sender = smarty.CustomHeaderSender({'X-Test': 'value'}, inner)
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smarty.SharedCredentials('shared-id', 'example.com').sign(smartyrequest)

        sender.send(smartyrequest)

        self.assertIs(smartyrequest, inner.request)
        self.assertEqual('https://example.com', inner.request.referer)
        self.assertEqual('shared-id', inner.request.parameters['key'])
        self.assertEqual('value', inner.request.headers['X-Test'])

    def test_appended_headers_are_joined_with_separator(self):
        sender = smarty.CustomHeaderSender(
            {'User-Agent': ['base-value', 'custom-value']},
            MockSender(None),
            {'User-Agent': ' '}
        )
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        sender.send(smartyrequest)

        self.assertEqual('base-value custom-value', smartyrequest.headers['User-Agent'])
