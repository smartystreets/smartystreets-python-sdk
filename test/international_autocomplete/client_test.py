import unittest

from smartystreets_python_sdk import Response, exceptions
from test.mocks import *
from smartystreets_python_sdk.international_autocomplete import Client, Lookup


class TestClient(unittest.TestCase):
    def test_sending_prefix_only_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)

        client.send(Lookup('1'))

        self.assertEqual('1', sender.request.parameters['search'])
        self.assertEqual(5, sender.request.parameters['max_results'])

    def test_sending_fully_populated_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.country = '2'
        lookup.max_results = 7
        lookup.locality = '3'
        lookup.postal_code = '4'
        lookup.address_id = '5'

        client.send(lookup)

        self.assertEqual('1', sender.request.parameters['search'])
        self.assertEqual('2', sender.request.parameters['country'])
        self.assertEqual(7, sender.request.parameters['max_results'])
        self.assertEqual('3', sender.request.parameters['include_only_locality'])
        self.assertEqual('4', sender.request.parameters['include_only_postal_code'])
        self.assertEqual('/5', sender.request.url_prefix)

    def test_deserialize_called_with_response_body(self):
        response = Response('Hello, World!', 0)

        sender = MockSender(response)
        deserializer = FakeDeserializer({})
        client = Client(sender, deserializer)

        client.send(Lookup('1'))

        self.assertEqual(response.payload, deserializer.input)

    def test_result_correctly_assigned_to_corresponding_lookup(self):
        lookup = Lookup('1')
        expected_result = {"candidates": [{"street": "2"}]}

        sender = MockSender(Response('{[]}', 0))
        deserializer = FakeDeserializer(expected_result)
        client = Client(sender, deserializer)

        client.send(lookup)

        self.assertEqual('2', lookup.result[0].street)

    def test_rejects_blank_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)

        self.assertRaises(exceptions.SmartyException, client.send, Lookup())

    def test_raises_exception_when_response_has_error(self):
        exception = exceptions.BadCredentialsError
        client = Client(MockExceptionSender(exception), FakeSerializer(None))

        self.assertRaises(exception, client.send, Lookup('test'))
