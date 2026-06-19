import unittest

from smartystreets_python_sdk.us_autocomplete_pro import Lookup, Client
from smartystreets_python_sdk.us_autocomplete_pro.source import Source
from test.mocks import *


class TestClient(unittest.TestCase):
    def test_sending_freeform_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup('123 main')
        lookup.add_custom_parameter('custom', '1')

        client.send(lookup)

        self.assertEqual('123 main', sender.request.parameters['search'])
        self.assertEqual('1', sender.request.parameters['custom'])

    def test_source_all_enum_serializes_as_string_value(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup('123 main')
        lookup.source = Source.ALL

        client.send(lookup)

        self.assertIs(type(sender.request.parameters['source']), str)
        self.assertEqual('all', sender.request.parameters['source'])

    def test_source_postal_enum_serializes_as_string_value(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup('123 main')
        lookup.source = Source.POSTAL

        client.send(lookup)

        self.assertIs(type(sender.request.parameters['source']), str)
        self.assertEqual('postal', sender.request.parameters['source'])

    def test_source_none_omits_parameter(self):
        sender = RequestCapturingSender()
        client = Client(sender, FakeDeserializer({}))
        lookup = Lookup('123 main')

        client.send(lookup)

        self.assertNotIn('source', sender.request.parameters)
