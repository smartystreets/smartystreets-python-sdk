import unittest

from smartystreets_python_sdk import URLPrefixSender
from smartystreets_python_sdk.us_enrichment.client import Client, send_lookup
from smartystreets_python_sdk.us_enrichment.lookup import PrincipalLookup, GeoReferenceLookup, SecondaryLookup, SecondaryCountLookup
from smartystreets_python_sdk.us_enrichment.response import Response
from test.mocks import *


class TestClient(unittest.TestCase):
    def test_sending_fully_populated_Enrichment_Lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)
        lookup = PrincipalLookup("xxx")
        lookup.add_custom_parameter('custom', '1')
        lookup.add_custom_parameter('custom2', '2')
        lookup.add_include_attribute('3')
        lookup.add_include_attribute('4')
        lookup.add_exclude_attribute('5')
        lookup.add_exclude_attribute('6')
        result = send_lookup(client, lookup)
        request = capturing_sender.request

        self.assertEqual("property", lookup.dataset)
        self.assertEqual("principal", lookup.dataSubset)
        self.assertEqual('1', request.parameters['custom'])
        self.assertEqual('2', request.parameters['custom2'])
        self.assertEqual('3,4', request.parameters['include'])
        self.assertEqual('5,6', request.parameters['exclude'])

        function_result = client.send_property_principal_lookup("xxx")
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

    def test_sending_principal_address_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = PrincipalLookup()
        lookup.street = "street"
        lookup.city = "city"
        lookup.state = "state"
        lookup.zipcode = "zipcode"
        result = send_lookup(client, lookup)

        self.assertEqual("property", lookup.dataset)
        self.assertEqual("principal", lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_property_principal_lookup(lookup)
        self.assertEqual(result, function_result)
    
    def test_sending_geo_reference_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = GeoReferenceLookup("xxx")
        result = send_lookup(client, lookup)

        self.assertEqual("geo-reference", lookup.dataset)
        self.assertEqual(None, lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_geo_reference_lookup("xxx")
        self.assertEqual(result, function_result)
    
    def test_sending_geo_reference_address_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = GeoReferenceLookup()
        lookup.street = "street"
        lookup.city = "city"
        lookup.state = "state"
        lookup.zipcode = "zipcode"
        result = send_lookup(client, lookup)

        self.assertEqual("geo-reference", lookup.dataset)
        self.assertEqual(None, lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_geo_reference_lookup(lookup)
        self.assertEqual(result, function_result)

    def test_sending_secondary_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = SecondaryLookup("xxx")
        result = send_lookup(client, lookup)

        self.assertEqual("secondary", lookup.dataset)
        self.assertEqual(None, lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_secondary_lookup("xxx")
        self.assertEqual(result, function_result)

    def test_sending_secondary_address_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = SecondaryLookup()
        lookup.street = "street"
        lookup.city = "city"
        lookup.state = "state"
        lookup.zipcode = "zipcode"
        result = send_lookup(client, lookup)

        self.assertEqual("secondary", lookup.dataset)
        self.assertEqual(None, lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_secondary_lookup(lookup)
        self.assertEqual(result, function_result)

    def test_sending_secondary_count_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = SecondaryCountLookup("xxx")
        result = send_lookup(client, lookup)

        self.assertEqual("secondary", lookup.dataset)
        self.assertEqual("count", lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_secondary_count_lookup("xxx")
        self.assertEqual(result, function_result)

    def test_sending_secondary_count_address_lookup(self):
        capturing_sender = RequestCapturingSender()
        sender = URLPrefixSender('http://localhost/', capturing_sender)
        serializer = FakeSerializer(None)
        client = Client(sender, serializer)

        lookup = SecondaryCountLookup()
        lookup.street = "street"
        lookup.city = "city"
        lookup.state = "state"
        lookup.zipcode = "zipcode"
        result = send_lookup(client, lookup)

        self.assertEqual("secondary", lookup.dataset)
        self.assertEqual("count", lookup.dataSubset)
        self.assertEqual(lookup.result, result)

        function_result = client.send_secondary_count_lookup(lookup)
        self.assertEqual(result, function_result)


class TestNotModified(unittest.TestCase):
    def test_304_is_success_with_refreshed_etag_and_untouched_results(self):
        from smartystreets_python_sdk import Response as HttpResponse, StatusCodeSender
        sender = StatusCodeSender(MockSender(HttpResponse("", 304, {'Etag': 'refreshed-etag'})))
        client = Client(sender, FakeSerializer(None))
        lookup = PrincipalLookup("xxx")
        lookup.request_etag = 'old-etag'
        lookup.result = ['prior']

        result = send_lookup(client, lookup)

        self.assertEqual('refreshed-etag', lookup.response_etag)
        self.assertEqual(['prior'], lookup.result)
        self.assertEqual(['prior'], result)
