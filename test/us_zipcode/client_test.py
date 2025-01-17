from test.mocks import RequestCapturingSender, FakeSerializer, FakeDeserializer, MockSender, MockExceptionSender
from smartystreets_python_sdk import Response, Batch, exceptions
from smartystreets_python_sdk.us_zipcode import Client, Lookup, Result


import unittest


class TestClient(unittest.TestCase):
    def test_single_lookup_values_correctly_assigned_to_parameters(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup()

        lookup.city = '0'
        lookup.state = '1'
        lookup.zipcode = '2'
        lookup.add_custom_parameter('custom', '3')

        client.send_lookup(lookup)

        self.assertEqual('0', sender.request.parameters['city'])
        self.assertEqual('1', sender.request.parameters['state'])
        self.assertEqual('2', sender.request.parameters['zipcode'])
        self.assertEqual('3', sender.request.parameters['custom'])

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

    def test_results_correctly_assigned_to_corresponding_lookup(self):
        raw_results = [{"input_index": 0}, {"input_index": 1}]
        expected_results = [Result(raw_results[0]), Result(raw_results[1])]
        batch = Batch()
        batch.add(Lookup())
        batch.add(Lookup())
        sender = MockSender(Response("[]", 0))
        deserializer = FakeDeserializer(raw_results)
        client = Client(sender, deserializer)

        client.send_batch(batch)

        self.assertEqual(expected_results[0].input_index, batch[0].result.input_index)
        self.assertEqual(expected_results[1].input_index, batch[1].result.input_index)

    def test_raises_exception_when_response_has_error(self):
        exception = exceptions.BadCredentialsError
        client = Client(MockExceptionSender(exception), FakeSerializer(None))

        self.assertRaises(exception, client.send_lookup, Lookup())
