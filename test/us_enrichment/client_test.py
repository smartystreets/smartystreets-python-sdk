import unittest

from smartystreets_python_sdk import URLPrefixSender
from smartystreets_python_sdk.us_enrichment.client import Client, send_lookup
from smartystreets_python_sdk.us_enrichment.lookup import FinancialLookup, PrincipalLookup
from smartystreets_python_sdk.us_enrichment.response import Response
from test.mocks import *


class TestClient(unittest.TestCase):
    def test_sending_Financial_Lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)
        lookup = FinancialLookup("xxx")
        result = send_lookup(client, lookup)

        self.assertEqual("property", lookup.dataset)
        self.assertEqual("financial", lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_property_financial_lookup("xxx")
        self.assertEqual(result, function_result)

    def test_sending_principal_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = PrincipalLookup("xxx")
        result = send_lookup(client, lookup)

        self.assertEqual("property", lookup.dataset)
        self.assertEqual("principal", lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_property_principal_lookup("xxx")
        self.assertEqual(result, function_result)
