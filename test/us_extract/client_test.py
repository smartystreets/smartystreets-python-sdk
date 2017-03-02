import unittest
from smartystreets_python_sdk import Response, exceptions, Batch
from smartystreets_python_sdk.us_extract import Client, Lookup, Address
from test.mocks import RequestCapturingSender, FakeSerializer, FakeDeserializer, MockSender, MockExceptionSender


class TestClient(unittest.TestCase):
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
        raw_addr_0 = {'api_output': [{'input_index': 0, 'candidate_index': 0}], 'verified': "true", 'text': 'Mister 0'}
        raw_addr_1 = {'api_output': [{'input_index': 1, 'candidate_index': 0}], 'verified': "true", 'text': 'Mister 1'}
        raw_addr_2 = {'api_output': [{'input_index': 1, 'candidate_index': 1}], 'verified': "true", 'text': 'Mister 2'}
        addresses = {'addresses': [raw_addr_0, raw_addr_1, raw_addr_2]}

        expected_addresses = [Address(raw_addr_0), Address(raw_addr_1), Address(raw_addr_2)]
        batch = Batch()
        batch.add(Lookup())
        batch.add(Lookup())
        sender = MockSender(Response("[]", 0))
        deserializer = FakeDeserializer(addresses)
        client = Client(sender, deserializer)

        client.send_batch(batch)

        self.assertEqual(expected_addresses[0].text, batch[0].result[0].text)
        self.assertEqual(expected_addresses[1].text, batch[1].result[0].text)
        self.assertEqual(expected_addresses[2].text, batch[1].result[1].text)

    def test_raises_exception_when_response_has_error(self):
        exception = exceptions.BadCredentialsError
        client = Client(MockExceptionSender(exception), FakeSerializer(None))

        self.assertRaises(exception, client.send_lookup, Lookup())
