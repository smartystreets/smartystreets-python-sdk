import unittest

from smartystreets_python_sdk import URLPrefixSender, Response, exceptions
from smartystreets_python_sdk.us_extract import Client, Lookup
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.us_extract import Result
from test.mocks import *


class TestClient(unittest.TestCase):
    def test_sending_body_only_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)
        expected_payload = 'Hello, World!'

        client.send(Lookup('Hello, World!'))

        self.assertEqual(expected_payload, capturing_sender.request.payload)

    def test_sending_fully_populated_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.html = True
        lookup.aggressive = True
        lookup.addresses_have_line_breaks = True
        lookup.addresses_per_line = 2
        lookup.add_custom_parameter('custom', '2')

        client.send(lookup)

        request = capturing_sender.request
        self.assertEqual('true', request.parameters['html'])
        self.assertEqual('true', request.parameters['aggressive'])
        self.assertEqual('true', request.parameters['addr_line_breaks'])
        self.assertEqual(2, request.parameters['addr_per_line'])
        self.assertEqual('2', request.parameters['custom'])

    def test_reject_blank_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        self.assertRaises(SmartyException, client.send, Lookup())

    def test_deserialize_called_with_response_body(self):
        response = Response('Hello, World!', 0)
        sender = MockSender(response)
        deserializer = FakeDeserializer({})
        client = Client(sender, deserializer)

        client.send(Lookup('Hello, World!'))

        self.assertEqual(response.payload, deserializer.input)

    def test_result_correctly_assigned_to_corresponding_lookup(self):
        raw_result = {"meta": {}, "addresses": [{"text": "Hello, World!"}]}
        expected_result = Result(raw_result)
        lookup = Lookup('Hello, World!')
        sender = MockSender(Response('[]', 0))
        deserializer = FakeDeserializer(raw_result)
        client = Client(sender, deserializer)

        client.send(lookup)

        self.assertEqual(expected_result.addresses[0].text, lookup.result.addresses[0].text)

    def test_content_type_set_correctly(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)
        lookup = Lookup("Hello, World!")

        client.send(lookup)

        self.assertEqual("text/plain", sender.request.content_type)

    def test_raises_exception_when_response_has_error(self):
        exception = exceptions.BadCredentialsError
        client = Client(MockExceptionSender(exception), FakeSerializer(None))

        self.assertRaises(exception, client.send, Lookup(text='test'))
