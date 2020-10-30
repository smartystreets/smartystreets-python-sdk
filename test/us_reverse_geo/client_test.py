import unittest

from smartystreets_python_sdk import Response
from smartystreets_python_sdk.exceptions import UnprocessableEntityError
from smartystreets_python_sdk.us_reverse_geo import Lookup, Client, Response
from test.mocks import *


class TestClient(unittest.TestCase):
    def test_sending_freeform_lookup(self):
        sender = RequestCapturingSender()
        serializer = FakeDeserializer({})
        client = Client(sender, serializer)
        lookup = Lookup(44.888888888, -111.111111111)

        client.send(lookup)

        self.assertEqual(44.88888889, sender.request.parameters['latitude'])
        self.assertEqual(-111.11111111, sender.request.parameters['longitude'])
