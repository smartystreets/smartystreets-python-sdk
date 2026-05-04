import smartystreets_python_sdk as smarty
import unittest
from test.mocks import *


class TestCustomHeaderSender(unittest.TestCase):

    def test_populates_headers(self):
        sender = smarty.RequestsSender()
        header = {'Test-User-Agent': 'Test-Agent', 'Test-Content-Type': 'Test-Content-Type'}
        sender = smarty.CustomHeaderSender(header, sender)

        self.assertEqual(sender.headers['Test-User-Agent'], 'Test-Agent')
        self.assertEqual(sender.headers['Test-Content-Type'], 'Test-Content-Type')

    def test_custom_headers_set(self):
        sender = smarty.CustomHeaderSender(
            {'Test-User-Agent': 'Test-Agent', 'Test-Content-Type': 'Test-Type'},
            MockSender(None)
        )
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        sender.send(smartyrequest)

        self.assertEqual('Test-Agent', smartyrequest.headers['Test-User-Agent'])
        self.assertEqual('Test-Type', smartyrequest.headers['Test-Content-Type'])

    def test_custom_headers_used(self):
        sender = smarty.CustomHeaderSender(
            {'User-Agent': 'Test-Agent', 'Content-Type': 'Test-Type'},
            MockSender(None)
        )
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        sender.send(smartyrequest)

        self.assertEqual('Test-Agent', smartyrequest.headers['User-Agent'])
        self.assertEqual('Test-Type', smartyrequest.headers['Content-Type'])

    def test_multiple_with_custom_header_calls_merge_headers(self):
        builder = smarty.ClientBuilder(None)
        builder.with_custom_header({'User-Agent': 'Test-Agent'})
        builder.with_custom_header({'Content-Type': 'Test-Type'})

        self.assertEqual('Test-Agent', builder.header['User-Agent'])
        self.assertEqual('Test-Type', builder.header['Content-Type'])

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
