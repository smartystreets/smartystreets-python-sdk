import unittest

from smartystreets_python_sdk import Response
from smartystreets_python_sdk.exceptions import UnprocessableEntityError
from smartystreets_python_sdk.us_reverse_geo import Lookup, Client, Response
from smartystreets_python_sdk.us_reverse_geo.source import Source
from test.mocks import *


class TestClient(unittest.TestCase):
    def test_sending_freeform_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup(44.888888888, -111.111111111)
        lookup.add_custom_parameter('custom', '1')

        client.send(lookup)

        self.assertEqual(44.88888889, sender.request.parameters['latitude'])
        self.assertEqual(-111.11111111, sender.request.parameters['longitude'])
        self.assertEqual('1', sender.request.parameters['custom'])

    def test_source_enum_serializes_as_string_value(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup(44.0, -111.0)
        lookup.source = Source.ALL

        client.send(lookup)

        self.assertIs(type(sender.request.parameters['source']), str)
        self.assertEqual('all', sender.request.parameters['source'])

    def test_source_postal_enum_serializes_as_string_value(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup(44.0, -111.0)
        lookup.source = Source.POSTAL

        client.send(lookup)

        self.assertIs(type(sender.request.parameters['source']), str)
        self.assertEqual('postal', sender.request.parameters['source'])

    def test_source_none_omits_parameter(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup(44.0, -111.0)

        client.send(lookup)

        self.assertNotIn('source', sender.request.parameters)
