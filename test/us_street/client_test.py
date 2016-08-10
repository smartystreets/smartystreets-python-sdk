import unittest
from smartystreets_python_sdk import Response
from smartystreets_python_sdk.us_street import Client, Lookup, Batch, Candidate
from test.mocks import RequestCapturingSender, FakeSerializer, FakeDeserializer, MockSender


class TestClient(unittest.TestCase):
    def test_sending_single_freeform_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer("")
        client = Client("http://localhost/", sender, serializer)

        client.send_lookup(Lookup("freeform"))

        self.assertEqual("http://localhost/", sender.request.urlprefix)
        self.assertEqual("freeform", sender.request.parameters['street'])

    def test_sending_single_fully_populated_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeSerializer("")
        client = Client("http://localhost/", sender, serializer)
        lookup = Lookup()
        lookup.addressee = "0"
        lookup.street = "1"
        lookup.secondary = "2"
        lookup.street2 = "3"
        lookup.urbanization = "4"
        lookup.city = "5"
        lookup.state = "6"
        lookup.zipcode = "7"
        lookup.lastline = "8"
        lookup.candidates = 9

        client.send_lookup(lookup)

        self.assertEqual("0", sender.request.parameters['addressee'])
        self.assertEqual("1", sender.request.parameters['street'])
        self.assertEqual("2", sender.request.parameters['secondary'])
        self.assertEqual("3", sender.request.parameters['street2'])
        self.assertEqual("4", sender.request.parameters['urbanization'])
        self.assertEqual("5", sender.request.parameters['city'])
        self.assertEqual("6", sender.request.parameters['state'])
        self.assertEqual("7", sender.request.parameters['zipcode'])
        self.assertEqual("8", sender.request.parameters['lastline'])
        self.assertEqual(9, sender.request.parameters['candidates'])

    def test_empty_batch_not_sent(self):
        sender = RequestCapturingSender()
        client = Client("/", sender, None)

        client.send_batch(Batch())

        self.assertIsNone(sender.request)

    def test_Successfully_Sends_Batch(self):
        expectedpayload = "Hello, World!"
        sender = RequestCapturingSender()
        serializer = FakeSerializer(expectedpayload)
        client = Client("http://localhost/", sender, serializer)
        batch = Batch()
        batch.add(Lookup())
        batch.add(Lookup())

        client.send_batch(batch)

        self.assertEqual(expectedpayload, sender.request.payload)

    def test_deserialize_called_with_response_body(self):
        response = Response("Hello, World!", 0)
        sender = MockSender(response)
        deserializer = FakeDeserializer(None)
        client = Client("/", sender, deserializer)

        client.send_lookup(Lookup())

        self.assertEqual(response.payload, deserializer.input)

    def test_Candidates_Correctly_Assigned_To_Corresponding_Lookup(self):
        expectedcandidates = [Candidate(0), Candidate(1), Candidate(1)]
        batch = Batch()
        batch.add(Lookup())
        batch.add(Lookup())
        sender = MockSender(Response("[]", 0))
        deserializer = FakeDeserializer(expectedcandidates)
        client = Client("/", sender, deserializer)

        client.send_batch(batch)

        self.assertEqual(expectedcandidates[0], batch[0].result[0])
        self.assertEqual(expectedcandidates[1], batch[1].result[0])
        self.assertEqual(expectedcandidates[2], batch[1].result[1])
