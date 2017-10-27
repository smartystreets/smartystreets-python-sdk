import unittest

from smartystreets_python_sdk import Response, exceptions
from test.mocks import *
from smartystreets_python_sdk.us_autocomplete import Client, Lookup, geolocation_type


class TestClient(unittest.TestCase):
    def test_sending_prefix_only_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)

        client.send(Lookup('1'))

        self.assertEqual('1', sender.request.parameters['prefix'])

    def test_sending_fully_populated_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.max_suggestions = 2
        lookup.add_city_filter('3')
        lookup.add_state_filter('4')
        lookup.add_prefer('5')
        lookup.prefer_ratio = .6
        lookup.geolocate_type = geolocation_type.STATE

        client.send(lookup)

        self.assertEqual('1', sender.request.parameters['prefix'])
        self.assertEqual(2, sender.request.parameters['suggestions'])
        self.assertEqual('3', sender.request.parameters['city_filter'])
        self.assertEqual('4', sender.request.parameters['state_filter'])
        self.assertEqual('5', sender.request.parameters['prefer'])
        self.assertEqual(.6, sender.request.parameters['prefer_ratio'])
        self.assertEqual('true', sender.request.parameters['geolocate'])
        self.assertEqual('state', sender.request.parameters['geolocate_precision'])

    def test_deserialize_called_with_response_body(self):
        response = Response('Hello, World!', 0)

        sender = MockSender(response)
        deserializer = FakeDeserializer({})
        client = Client(sender, deserializer)

        client.send(Lookup('1'))

        self.assertEqual(response.payload, deserializer.input)

    def test_result_correctly_assigned_to_corresponding_lookup(self):
        lookup = Lookup('1')
        expected_result = {"suggestions": [{"text": "2"}]}

        sender = MockSender(Response('{[]}', 0))
        deserializer = FakeDeserializer(expected_result)
        client = Client(sender, deserializer)

        client.send(lookup)

        self.assertEqual('2', lookup.result[0].text)

    def test_rejects_blank_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)

        self.assertRaises(exceptions.SmartyException, client.send, Lookup())

    def test_raises_exception_when_response_has_error(self):
        exception = exceptions.BadCredentialsError
        client = Client(MockExceptionSender(exception), FakeSerializer(None))

        self.assertRaises(exception, client.send, Lookup(prefix='test'))
