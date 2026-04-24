import unittest

from smartystreets_python_sdk import Response, URLPrefixSender
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.us_enrichment import BusinessLookup, BusinessSummaryResponse
from smartystreets_python_sdk.us_enrichment.client import Client
from test.mocks import FakeDeserializer, FakeSerializer, MockSender, RequestCapturingSender


class TestBusinessSummary(unittest.TestCase):
    def _client(self, inner_sender, serializer=None):
        if serializer is None:
            serializer = FakeSerializer(None)
        sender = URLPrefixSender('http://localhost/', inner_sender)
        return Client(sender, serializer), inner_sender

    def test_business_lookup_with_smartykey_builds_url(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        result = client.send_business_lookup("1")

        self.assertEqual("1/business", capturing.request.url_components)
        self.assertEqual(result, [])

    def test_business_lookup_with_components_builds_url(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessLookup()
        lookup.street = "street"
        lookup.city = "city"
        lookup.state = "state"
        lookup.zipcode = "zipcode"
        client.send_business_lookup(lookup)

        self.assertEqual("search/business", capturing.request.url_components)
        self.assertEqual("street", capturing.request.parameters['street'])
        self.assertEqual("city", capturing.request.parameters['city'])
        self.assertEqual("state", capturing.request.parameters['state'])
        self.assertEqual("zipcode", capturing.request.parameters['zipcode'])

    def test_business_lookup_with_freeform_builds_url(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessLookup()
        lookup.freeform = "1600 amphitheatre pkwy mountain view ca"
        client.send_business_lookup(lookup)

        self.assertEqual("search/business", capturing.request.url_components)
        self.assertEqual(
            "1600 amphitheatre pkwy mountain view ca",
            capturing.request.parameters['freeform'],
        )

    def test_rejects_whitespace_smartykey_on_summary_lookup(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        with self.assertRaises(SmartyException):
            client.send_business_lookup("   ")

    def test_rejects_whitespace_on_all_standard_lookup_fields(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessLookup("   ")
        lookup.street = "   "
        lookup.freeform = "   "

        with self.assertRaises(SmartyException):
            client.send_business_lookup(lookup)

    def test_enrichment_summary_lookup_sends_etag_header(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessLookup("1")
        lookup.request_etag = "abc-etag-123"
        client.send_business_lookup(lookup)

        self.assertEqual("abc-etag-123", capturing.request.headers['Etag'])

    def test_summary_captures_response_etag_on_lookup(self):
        response = Response("[]", 200, {'Etag': 'server-etag-1'})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer([]))

        lookup = BusinessLookup("1")
        client.send_business_lookup(lookup)

        self.assertEqual("server-etag-1", lookup.response_etag)

    def test_response_etag_none_when_header_absent(self):
        response = Response("[]", 200, {})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer([]))

        lookup = BusinessLookup("1")
        client.send_business_lookup(lookup)

        self.assertIsNone(lookup.response_etag)

    def test_business_lookup_deserializes_response(self):
        payload = [
            {
                'smarty_key': '1',
                'data_set_name': 'business',
                'businesses': [
                    {'company_name': 'Acme Co', 'business_id': 'B-1'},
                    {'company_name': 'Widget Inc', 'business_id': 'B-2'},
                ],
            }
        ]
        response = Response("[]", 200, {})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer(payload))

        result = client.send_business_lookup("1")

        self.assertEqual(1, len(result))
        self.assertIsInstance(result[0], BusinessSummaryResponse)
        self.assertEqual('1', result[0].smarty_key)
        self.assertEqual(2, len(result[0].businesses))
        self.assertEqual('Acme Co', result[0].businesses[0].company_name)
        self.assertEqual('B-2', result[0].businesses[1].business_id)


if __name__ == '__main__':
    unittest.main()
