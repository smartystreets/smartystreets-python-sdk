import unittest

from smartystreets_python_sdk import Response, exceptions
from test.mocks import *
from smartystreets_python_sdk.us_autocomplete import Client, Lookup, geolocation_type
from smartystreets_python_sdk.us_autocomplete.source import Source


class TestClient(unittest.TestCase):
    def test_sending_search_only_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)

        client.send(Lookup('1'))

        self.assertEqual('1', sender.request.parameters['search'])

    def test_sending_fully_populated_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.max_results = 7
        lookup.add_city_filter('city1')
        lookup.add_city_filter('city2')
        lookup.add_state_filter('state1')
        lookup.add_state_filter('state2')
        lookup.add_state_exclusion('state3')
        lookup.add_city_preference('city3')
        lookup.add_state_preference('state4')
        lookup.prefer_ratio = 3
        lookup.prefer_geolocation = geolocation_type.CITY
        lookup.source = Source.ALL
        lookup.selected = 'selectedAddress'
        lookup.exclude = ['excludedAddress']
        lookup.add_custom_parameter('custom', '6')

        client.send(lookup)

        self.assertEqual('1', sender.request.parameters['search'])
        self.assertEqual(7, sender.request.parameters['max_results'])
        self.assertEqual('city1;city2', sender.request.parameters['include_only_cities'])
        self.assertEqual('state1;state2', sender.request.parameters['include_only_states'])
        self.assertEqual('state3', sender.request.parameters['exclude_states'])
        self.assertEqual('city3', sender.request.parameters['prefer_cities'])
        self.assertEqual('state4', sender.request.parameters['prefer_states'])
        self.assertEqual(3, sender.request.parameters['prefer_ratio'])
        self.assertEqual('city', sender.request.parameters['prefer_geolocation'])
        self.assertEqual('all', sender.request.parameters['source'])
        self.assertEqual('selectedAddress', sender.request.parameters['selected'])
        self.assertEqual('excludedAddress', sender.request.parameters['exclude'])
        self.assertEqual('6', sender.request.parameters['custom'])

    def test_sending_exclude(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.exclude = ['excluded1', 'excluded2', 'excluded3']

        client.send(lookup)

        self.assertEqual('excluded1,excluded2,excluded3', sender.request.parameters['exclude'])

    def test_prefer_geolocation_none_is_omitted(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.prefer_geolocation = geolocation_type.NONE

        client.send(lookup)

        self.assertNotIn('prefer_geolocation', sender.request.parameters)

    def test_zip_filter_serialized(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.add_zip_filter('11111')

        client.send(lookup)

        self.assertEqual('11111', sender.request.parameters['include_only_zip_codes'])
        self.assertNotIn('prefer_geolocation', sender.request.parameters)

    def test_prefer_zip_serialized(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1')
        lookup.add_zip_preference('22222')

        client.send(lookup)

        self.assertEqual('22222', sender.request.parameters['prefer_zip_codes'])
        self.assertNotIn('prefer_geolocation', sender.request.parameters)

    def test_source_omitted_when_unset(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)

        client.send(Lookup('1'))

        self.assertNotIn('source', sender.request.parameters)

    def test_source_all_enum_serializes_as_string_value(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup('1')
        lookup.source = Source.ALL

        client.send(lookup)

        self.assertIs(type(sender.request.parameters['source']), str)
        self.assertEqual('all', sender.request.parameters['source'])

    def test_source_postal_enum_serializes_as_string_value(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup('1')
        lookup.source = Source.POSTAL

        client.send(lookup)

        self.assertIs(type(sender.request.parameters['source']), str)
        self.assertEqual('postal', sender.request.parameters['source'])

    def test_source_none_omits_parameter(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup('1')

        client.send(lookup)

        self.assertNotIn('source', sender.request.parameters)

    def test_deserialize_called_with_response_body(self):
        response = Response('Hello, World!', 0)

        sender = MockSender(response)
        deserializer = FakeDeserializer({})
        client = Client(sender, deserializer)

        client.send(Lookup('1'))

        self.assertEqual(response.payload, deserializer.input)

    def test_result_correctly_assigned_to_corresponding_lookup(self):
        lookup = Lookup('1')
        expected_result = {"suggestions": [{"street_line": "2", "entry_id": "3"}]}

        sender = MockSender(Response('{[]}', 0))
        deserializer = FakeDeserializer(expected_result)
        client = Client(sender, deserializer)

        client.send(lookup)

        self.assertEqual('2', lookup.result[0].street_line)
        self.assertEqual('3', lookup.result[0].entry_id)

    def test_all_suggestion_fields_deserialized(self):
        lookup = Lookup('1')
        expected_result = {"suggestions": [{
            "smarty_key": "key",
            "entry_id": "entry",
            "street_line": "street",
            "secondary": "secondary",
            "city": "city",
            "state": "state",
            "zipcode": "zip",
            "entries": 5,
        }]}

        sender = MockSender(Response('{[]}', 0))
        deserializer = FakeDeserializer(expected_result)
        client = Client(sender, deserializer)

        client.send(lookup)

        suggestion = lookup.result[0]
        self.assertEqual('key', suggestion.smarty_key)
        self.assertEqual('entry', suggestion.entry_id)
        self.assertEqual('street', suggestion.street_line)
        self.assertEqual('secondary', suggestion.secondary)
        self.assertEqual('city', suggestion.city)
        self.assertEqual('state', suggestion.state)
        self.assertEqual('zip', suggestion.zipcode)
        self.assertEqual(5, suggestion.entries)

    def test_rejects_blank_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer({})
        client = Client(sender, serializer)

        self.assertRaises(exceptions.SmartyException, client.send, Lookup())

    def test_raises_exception_when_response_has_error(self):
        exception = exceptions.BadCredentialsError
        client = Client(MockExceptionSender(exception), FakeSerializer(None))

        self.assertRaises(exception, client.send, Lookup('test'))
