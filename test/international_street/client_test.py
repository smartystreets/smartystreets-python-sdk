import unittest

from smartystreets_python_sdk import Response
from smartystreets_python_sdk.exceptions import UnprocessableEntityError
from smartystreets_python_sdk.international_street import Lookup, Client, language_mode, Candidate
from test.mocks import *


class TestClient(unittest.TestCase):
    def test_sending_freeform_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup('1', '2')

        client.send(lookup)

        self.assertEqual('1', sender.request.parameters['freeform'])
        self.assertEqual('2', sender.request.parameters['country'])

    def test_sending_single_fully_populated_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup()
        lookup.country = '0'
        lookup.geocode = True
        lookup.language = language_mode.NATIVE
        lookup.freeform = '1'
        lookup.address1 = '2'
        lookup.address2 = '3'
        lookup.address3 = '4'
        lookup.address4 = '5'
        lookup.unit = '5.1'
        lookup.organization = '6'
        lookup.locality = '7'
        lookup.administrative_area = '8'
        lookup.postal_code = '9'

        client.send(lookup)

        self.assertEqual('0', sender.request.parameters['country'])
        self.assertEqual('true', sender.request.parameters['geocode'])
        self.assertEqual(language_mode.NATIVE, sender.request.parameters['language'])
        self.assertEqual('1', sender.request.parameters['freeform'])
        self.assertEqual('2', sender.request.parameters['address1'])
        self.assertEqual('3', sender.request.parameters['address2'])
        self.assertEqual('4', sender.request.parameters['address3'])
        self.assertEqual('5', sender.request.parameters['address4'])
        self.assertEqual('5.1', sender.request.parameters['unit'])
        self.assertEqual('6', sender.request.parameters['organization'])
        self.assertEqual('7', sender.request.parameters['locality'])
        self.assertEqual('8', sender.request.parameters['administrative_area'])
        self.assertEqual('9', sender.request.parameters['postal_code'])

    def test_empty_lookup_rejected(self):
        sender = MockSender(None)
        client = Client(sender, None)

        self.assertRaises(UnprocessableEntityError, client.send, Lookup())

    def test_rejects_lookups_with_only_country(self):
        sender = MockSender(None)
        client = Client(sender, None)
        lookup = Lookup(None, '0')

        self.assertRaises(UnprocessableEntityError, client.send, lookup)

    def test_rejects_lookups_with_only_country_and_address1(self):
        sender = MockSender(None)
        client = Client(sender, None)
        lookup = Lookup(None, '0')
        lookup.address1 = '1'

        self.assertRaises(UnprocessableEntityError, client.send, lookup)

    def test_rejects_lookups_with_only_country_and_address1_and_locality(self):
        sender = MockSender(None)
        client = Client(sender, None)
        lookup = Lookup(None, '0')
        lookup.address1 = '1'
        lookup.locality = '2'

        self.assertRaises(UnprocessableEntityError, client.send, lookup)

    def test_rejects_lookups_with_only_country_and_address1_and_administrative_area(self):
        sender = MockSender(None)
        client = Client(sender, None)
        lookup = Lookup(None, '0')
        lookup.address1 = '1'
        lookup.administrative_area = '2'

        self.assertRaises(UnprocessableEntityError, client.send, lookup)

    def test_accepts_lookups_with_enough_info(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)
        lookup = Lookup()

        lookup.country = '0'
        lookup.freeform = '1'
        client.send(lookup)

        lookup.freeform = None
        lookup.address1 = '1'
        lookup.postal_code = '2'
        client.send(lookup)

        lookup.postal_code = None
        lookup.locality = '3'
        lookup.administrative_area = '4'
        client.send(lookup)

    def test_deserialize_called_with_response_body(self):
        response = Response('Hello, World!', 0)

        sender = MockSender(response)
        deserializer = FakeDeserializer({})
        client = Client(sender, deserializer)

        client.send(Lookup('1', '2'))

        self.assertEqual(response.payload, deserializer.input)

    def test_candidates_correctly_assigned_to_lookup(self):
        raw_candidates = [{'address1': 'street 1'}, {'address1': 'street 2'}]
        expected_candidates = [Candidate(raw_candidates[0]), Candidate(raw_candidates[1])]
        lookup = Lookup('1', '2')
        sender = MockSender(Response('[]', 0))
        deserializer = FakeDeserializer(raw_candidates)
        client = Client(sender, deserializer)

        client.send(lookup)

        self.assertEqual(expected_candidates[0].address1, lookup.result[0].address1)
        self.assertEqual(expected_candidates[1].address1, lookup.result[1].address1)
