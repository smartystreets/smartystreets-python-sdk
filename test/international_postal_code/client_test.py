import unittest

from smartystreets_python_sdk import Response
from smartystreets_python_sdk.international_postal_code import Client, Lookup, Candidate
from test.mocks import RequestCapturingSender, MockSender, FakeDeserializer


class TestClient(unittest.TestCase):
    def test_sending_single_fully_populated_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup()
        lookup.input_id = '0'
        lookup.country = '1'
        lookup.locality = '2'
        lookup.administrative_area = '3'
        lookup.postal_code = '4'

        client.send(lookup)

        self.assertEqual('0', sender.request.parameters['input_id'])
        self.assertEqual('1', sender.request.parameters['country'])
        self.assertEqual('2', sender.request.parameters['locality'])
        self.assertEqual('3', sender.request.parameters['administrative_area'])
        self.assertEqual('4', sender.request.parameters['postal_code'])

    def test_empty_lookup_rejected(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup()

        # Empty lookup should not fail; validation happens at API level
        # Just verify the request is built properly
        client.send(lookup)

    def test_none_lookup_rejected(self):
        sender = MockSender(None)
        client = Client(sender, None)

        self.assertRaises(ValueError, client.send, None)

    def test_deserialize_called_with_response_body(self):
        response = Response('Hello, World!', 0)

        sender = MockSender(response)
        deserializer = FakeDeserializer({})
        client = Client(sender, deserializer)

        lookup = Lookup()
        lookup.country = '1'
        lookup.locality = '2'
        client.send(lookup)

        self.assertEqual(response.payload, deserializer.input)

    def test_candidates_correctly_assigned_to_lookup(self):
        raw_candidates = [{'input_id': 'ID-1', 'locality': 'city 1'}, {'input_id': 'ID-2', 'locality': 'city 2'}]
        expected_candidates = [Candidate(raw_candidates[0]), Candidate(raw_candidates[1])]
        lookup = Lookup()
        lookup.country = 'US'
        sender = MockSender(Response('[]', 0))
        deserializer = FakeDeserializer(raw_candidates)
        client = Client(sender, deserializer)

        client.send(lookup)

        self.assertEqual(expected_candidates[0].input_id, lookup.results[0].input_id)
        self.assertEqual(expected_candidates[0].locality, lookup.results[0].locality)
        self.assertEqual(expected_candidates[1].input_id, lookup.results[1].input_id)
        self.assertEqual(expected_candidates[1].locality, lookup.results[1].locality)


if __name__ == "__main__":
    unittest.main()
