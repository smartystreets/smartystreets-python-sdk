import unittest

from smartystreets_python_sdk import Response, URLPrefixSender
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.us_enrichment import BusinessDetailLookup, BusinessDetailResponse
from smartystreets_python_sdk.us_enrichment.client import Client
from test.mocks import FakeDeserializer, FakeSerializer, MockSender, RequestCapturingSender


class TestBusinessDetail(unittest.TestCase):
    def _client(self, inner_sender, serializer=None):
        if serializer is None:
            serializer = FakeSerializer(None)
        sender = URLPrefixSender('http://localhost/', inner_sender)
        return Client(sender, serializer), inner_sender

    def test_business_detail_builds_url(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        client.send_business_detail_lookup("ABC123")

        self.assertEqual("business/ABC123", capturing.request.url_components)

    def test_business_detail_url_encodes_reserved_chars(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        client.send_business_detail_lookup("a/b?c#d")

        self.assertEqual("business/a%2Fb%3Fc%23d", capturing.request.url_components)

    def test_business_detail_sends_etag_header(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessDetailLookup("ABC123")
        lookup.request_etag = "xyz-789"
        client.send_business_detail_lookup(lookup)

        self.assertEqual("xyz-789", capturing.request.headers['Etag'])

    def test_business_detail_include_fields_in_params(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessDetailLookup("ABC123")
        lookup.add_include_attribute("phone")
        client.send_business_detail_lookup(lookup)

        self.assertEqual("phone", capturing.request.parameters['include'])

    def test_business_detail_exclude_fields_in_params(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessDetailLookup("ABC123")
        lookup.add_exclude_attribute("phone")
        client.send_business_detail_lookup(lookup)

        self.assertEqual("phone", capturing.request.parameters['exclude'])

    def test_business_detail_custom_parameters_in_params(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessDetailLookup("ABC123")
        lookup.add_custom_parameter("custom", "value")
        client.send_business_detail_lookup(lookup)

        self.assertEqual("value", capturing.request.parameters['custom'])

    def test_business_detail_include_exclude_custom_combined(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        lookup = BusinessDetailLookup("ABC123")
        lookup.add_include_attribute("phone")
        lookup.add_include_attribute("email")
        lookup.add_exclude_attribute("fax")
        lookup.add_custom_parameter("custom", "value")
        client.send_business_detail_lookup(lookup)

        self.assertEqual("phone,email", capturing.request.parameters['include'])
        self.assertEqual("fax", capturing.request.parameters['exclude'])
        self.assertEqual("value", capturing.request.parameters['custom'])

    def test_business_detail_rejects_empty_business_id(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        with self.assertRaises(SmartyException):
            client.send_business_detail_lookup("")

    def test_business_detail_rejects_none_business_id(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        with self.assertRaises(SmartyException):
            client.send_business_detail_lookup(BusinessDetailLookup(None))

    def test_business_detail_rejects_whitespace_business_id(self):
        capturing = RequestCapturingSender()
        client, _ = self._client(capturing)

        with self.assertRaises(SmartyException):
            client.send_business_detail_lookup("   ")

    def test_business_detail_rejects_multiple_results(self):
        response = Response("[]", 200, {})
        mock = MockSender(response)
        client, _ = self._client(
            mock,
            serializer=FakeDeserializer([
                {'smarty_key': '1', 'business_id': 'B1'},
                {'smarty_key': '1', 'business_id': 'B2'},
            ]),
        )

        with self.assertRaises(SmartyException):
            client.send_business_detail_lookup("ABC123")

    def test_business_detail_accepts_single_result(self):
        payload = [{
            'smarty_key': 'key-1',
            'data_set_name': 'business',
            'business_id': 'B-1',
            'attributes': {
                'company_name': 'Acme Co',
                'phone': '555-1212',
            },
        }]
        response = Response("[]", 200, {})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer(payload))

        result = client.send_business_detail_lookup("ABC123")

        self.assertIsInstance(result, BusinessDetailResponse)
        self.assertEqual('key-1', result.smarty_key)
        self.assertEqual('B-1', result.business_id)
        self.assertEqual('Acme Co', result.attributes.company_name)
        self.assertEqual('555-1212', result.attributes.phone)

    def test_business_detail_accepts_empty_results(self):
        response = Response("[]", 200, {})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer([]))

        result = client.send_business_detail_lookup("ABC123")

        self.assertIsNone(result)

    def test_business_detail_captures_response_etag(self):
        response = Response("[]", 200, {'Etag': 'server-etag-1'})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer([]))

        lookup = BusinessDetailLookup("ABC123")
        client.send_business_detail_lookup(lookup)

        self.assertEqual('server-etag-1', lookup.response_etag)

    def test_response_etag_does_not_clobber_request_etag(self):
        response = Response("[]", 200, {'Etag': 'server-etag-1'})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer([]))

        lookup = BusinessDetailLookup("ABC123")
        lookup.request_etag = "client-etag"
        client.send_business_detail_lookup(lookup)

        self.assertEqual('client-etag', lookup.request_etag)
        self.assertEqual('server-etag-1', lookup.response_etag)

    def test_business_detail_case_insensitive_response_etag_header(self):
        response = Response("[]", 200, {'ETag': 'case-insensitive-etag'})
        mock = MockSender(response)
        client, _ = self._client(mock, serializer=FakeDeserializer([]))

        lookup = BusinessDetailLookup("ABC123")
        client.send_business_detail_lookup(lookup)

        self.assertEqual('case-insensitive-etag', lookup.response_etag)


if __name__ == '__main__':
    unittest.main()
