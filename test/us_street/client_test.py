import unittest
from smartystreets_python_sdk import Response, exceptions, Batch
from smartystreets_python_sdk.us_street import Client, Lookup, Candidate, match_type
from test.mocks import RequestCapturingSender, FakeSerializer, FakeDeserializer, MockSender, MockExceptionSender


class TestClient(unittest.TestCase):
    def test_freeform_assigned_to_street_field(self):
        lookup = Lookup("freeform address")

        self.assertEqual("freeform address", lookup.street)

    def test_single_lookup_values_correctly_assigned_to_parameters(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup()

        lookup.street = '0'
        lookup.street2 = '1'
        lookup.secondary = '2'
        lookup.city = '3'
        lookup.state = '4'
        lookup.zipcode = '5'
        lookup.lastline = '6'
        lookup.addressee = '7'
        lookup.urbanization = '8'
        lookup.match = match_type.INVALID
        lookup.candidates = '9'

        client.send_lookup(lookup)

        self.assertEqual('0', sender.request.parameters['street'])
        self.assertEqual('1', sender.request.parameters['street2'])
        self.assertEqual('2', sender.request.parameters['secondary'])
        self.assertEqual('3', sender.request.parameters['city'])
        self.assertEqual('4', sender.request.parameters['state'])
        self.assertEqual('5', sender.request.parameters['zipcode'])
        self.assertEqual('6', sender.request.parameters['lastline'])
        self.assertEqual('7', sender.request.parameters['addressee'])
        self.assertEqual('8', sender.request.parameters['urbanization'])
        self.assertEqual(match_type.INVALID, sender.request.parameters['match'])
        self.assertEqual('9', sender.request.parameters['candidates'])

    def test_empty_batch_not_sent(self):
        sender = RequestCapturingSender()
        client = Client(sender, None)

        client.send_batch(Batch())

        self.assertIsNone(sender.request)

    def test_successfully_sends_batch(self):
        expected_payload = "Hello, World!"
        sender = RequestCapturingSender()
        serializer = FakeSerializer(expected_payload)
        client = Client(sender, serializer)
        batch = Batch()
        batch.add(Lookup())
        batch.add(Lookup())

        client.send_batch(batch)

        self.assertEqual(expected_payload, sender.request.payload)

    def test_deserialize_called_with_response_body(self):
        response = Response("Hello, World!", 0)
        sender = MockSender(response)
        deserializer = FakeDeserializer(None)
        client = Client(sender, deserializer)

        client.send_lookup(Lookup())

        self.assertEqual(response.payload, deserializer.input)

    def test_candidates_correctly_assigned_to_corresponding_lookup(self):
        candidate0 = {'input_index': 0, 'candidate_index': 0, 'addressee': 'Mister 0'}
        candidate1 = {'input_index': 1, 'candidate_index': 0, 'addressee': 'Mister 1'}
        candidate2 = {'input_index': 1, 'candidate_index': 1, 'addressee': 'Mister 2'}
        raw_candidates = [candidate0, candidate1, candidate2]

        expected_candidates = [Candidate(candidate0), Candidate(candidate1), Candidate(candidate2)]
        batch = Batch()
        batch.add(Lookup())
        batch.add(Lookup())
        sender = MockSender(Response("[]", 0))
        deserializer = FakeDeserializer(raw_candidates)
        client = Client(sender, deserializer)

        client.send_batch(batch)

        self.assertEqual(expected_candidates[0].addressee, batch[0].result[0].addressee)
        self.assertEqual(expected_candidates[1].addressee, batch[1].result[0].addressee)
        self.assertEqual(expected_candidates[2].addressee, batch[1].result[1].addressee)

    def test_raises_exception_when_response_has_error(self):
        exception = exceptions.BadCredentialsError
        client = Client(MockExceptionSender(exception), FakeSerializer(None))

        self.assertRaises(exception, client.send_lookup, Lookup())
