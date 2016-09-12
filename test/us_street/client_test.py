import json
import unittest
from smartystreets_python_sdk import Response
from smartystreets_python_sdk.us_street import Client, Lookup, Batch, Candidate
from test.mocks import RequestCapturingSender, FakeSerializer, FakeDeserializer, MockSender


class TestClient(unittest.TestCase):
    def test_freeform_assigned_to_street_field(self):
        lookup = Lookup("freeform address")

        self.assertEqual("freeform address", lookup.street)

    def test_empty_batch_not_sent(self):
        sender = RequestCapturingSender()
        client = Client(sender, None)

        client.send_batch(Batch())

        self.assertIsNone(sender.request)

    def test_Successfully_Sends_Batch(self):
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

    def test_Candidates_Correctly_Assigned_To_Corresponding_Lookup(self):
        expected_candidates = [Candidate(0), Candidate(1), Candidate(1)]
        batch = Batch()
        batch.add(Lookup())
        batch.add(Lookup())
        sender = MockSender(Response("[]", 0))
        deserializer = FakeDeserializer(expected_candidates)
        client = Client(sender, deserializer)

        client.send_batch(batch)

        self.assertEqual(expected_candidates[0], batch[0].result[0])
        self.assertEqual(expected_candidates[1], batch[1].result[0])
        self.assertEqual(expected_candidates[2], batch[1].result[1])
