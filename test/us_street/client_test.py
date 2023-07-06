import unittest

from smartystreets_python_sdk import Response, exceptions, Batch, native_serializer
from smartystreets_python_sdk.us_street import Client, Lookup, Candidate
from smartystreets_python_sdk.us_street.match_type import MatchType
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
        lookup.street2 = '1.1'
        lookup.secondary = '2'
        lookup.city = '3'
        lookup.state = '4'
        lookup.zipcode = '5'
        lookup.lastline = '6'
        lookup.addressee = '7'
        lookup.urbanization = '8'
        lookup.match = MatchType.ENHANCED
        lookup.candidates = 1

        client.send_lookup(lookup)

        self.assertEqual('0', sender.request.parameters['street'])
        self.assertEqual('1.1', sender.request.parameters['street2'])
        self.assertEqual('2', sender.request.parameters['secondary'])
        self.assertEqual('3', sender.request.parameters['city'])
        self.assertEqual('4', sender.request.parameters['state'])
        self.assertEqual('5', sender.request.parameters['zipcode'])
        self.assertEqual('6', sender.request.parameters['lastline'])
        self.assertEqual('7', sender.request.parameters['addressee'])
        self.assertEqual('8', sender.request.parameters['urbanization'])
        self.assertEqual(MatchType.ENHANCED.value, sender.request.parameters['match'])
        self.assertEqual(5, sender.request.parameters['candidates'])

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

    def test_full_json_response_deserialization(self):
        body = """{
                "input_id": "blah",
                "input_index": 0,
                "candidate_index": 4242,
                "addressee": "John Smith",
                "delivery_line_1": "3214 N University Ave # 409",
                "delivery_line_2": "blah blah",
                "last_line": "Provo UT 84604-4405",
                "delivery_point_barcode": "846044405140",
                "smarty_key": "1750774478",
                "components": {
                    "primary_number": "3214",
                    "street_predirection": "N",
                    "street_postdirection": "Q",
                    "street_name": "University",
                    "street_suffix": "Ave",
                    "secondary_number": "409",
                    "secondary_designator": "#",
                    "extra_secondary_number": "410",
                    "extra_secondary_designator": "Apt",
                    "pmb_number": "411",
                    "pmb_designator": "Box",
                    "city_name": "Provo",
                    "default_city_name": "Provo",
                    "state_abbreviation": "UT",
                    "zipcode": "84604",
                    "plus4_code": "4405",
                    "delivery_point": "14",
                    "delivery_point_check_digit": "0",
                    "urbanization": "urbanization"
                },
                "metadata": {
                    "record_type": "S",
                    "zip_type": "Standard",
                    "county_fips": "49049",
                    "county_name": "Utah",
                    "carrier_route": "C016",
                    "congressional_district": "03",
                    "building_default_indicator": "hi",
                    "rdi": "Commercial",
                    "elot_sequence": "0016",
                    "elot_sort": "A",
                    "latitude": 40.27658,
                    "longitude": -111.65759,
                    "coordinate_license": 1, 
                    "precision": "Zip9",
                    "time_zone": "Mountain",
                    "utc_offset": -7,
                    "dst": true,
                    "ews_match": true
                },
                "analysis": {
                    "dpv_match_code": "S",
                    "dpv_footnotes": "AACCRR",
                    "dpv_cmra": "Y",
                    "dpv_vacant": "N",
                    "active": "Y",
                    "dpv_no_stat": "N",
                    "footnotes": "footnotes",
                    "lacslink_code": "lacslink_code",
                    "lacslink_indicator": "lacslink_indicator",
                    "suitelink_match": true,
                    "enhanced_match": "enhanced_match"
                }
            }"""

        object = native_serializer.NativeSerializer().deserialize(body)
        actual_candidate = Candidate(object)
        self.assertEqual(actual_candidate.input_id, "blah")
        self.assertEqual(actual_candidate.input_index, 0)
        self.assertEqual(actual_candidate.candidate_index, 4242)
        self.assertEqual(actual_candidate.addressee, "John Smith")
        self.assertEqual(actual_candidate.delivery_line_1, "3214 N University Ave # 409")
        self.assertEqual(actual_candidate.delivery_line_2, "blah blah")
        self.assertEqual(actual_candidate.last_line, "Provo UT 84604-4405")
        self.assertEqual(actual_candidate.delivery_point_barcode, "846044405140")
        self.assertEqual(actual_candidate.smarty_key, "1750774478")
        self.assertEqual(actual_candidate.components.primary_number, "3214")
        self.assertEqual(actual_candidate.components.street_predirection, "N")
        self.assertEqual(actual_candidate.components.street_name, "University")
        self.assertEqual(actual_candidate.components.street_postdirection, "Q")
        self.assertEqual(actual_candidate.components.street_suffix, "Ave")
        self.assertEqual(actual_candidate.components.secondary_number, "409")
        self.assertEqual(actual_candidate.components.secondary_designator, "#")
        self.assertEqual(actual_candidate.components.extra_secondary_number, "410")
        self.assertEqual(actual_candidate.components.extra_secondary_designator, "Apt")
        self.assertEqual(actual_candidate.components.pmb_number, "411")
        self.assertEqual(actual_candidate.components.pmb_designator, "Box")
        self.assertEqual(actual_candidate.components.city_name, "Provo")
        self.assertEqual(actual_candidate.components.default_city_name, "Provo")
        self.assertEqual(actual_candidate.components.state_abbreviation, "UT")
        self.assertEqual(actual_candidate.components.zipcode, "84604")
        self.assertEqual(actual_candidate.components.plus4_code, "4405")
        self.assertEqual(actual_candidate.components.delivery_point, "14")
        self.assertEqual(actual_candidate.components.delivery_point_check_digit, "0")
        self.assertEqual(actual_candidate.components.urbanization, "urbanization")
        self.assertEqual(actual_candidate.metadata.record_type, "S")
        self.assertEqual(actual_candidate.metadata.zip_type, "Standard")
        self.assertEqual(actual_candidate.metadata.county_fips, "49049")
        self.assertEqual(actual_candidate.metadata.county_name, "Utah")
        self.assertEqual(actual_candidate.metadata.carrier_route, "C016")
        self.assertEqual(actual_candidate.metadata.congressional_district, "03")
        self.assertEqual(actual_candidate.metadata.building_default_indicator, "hi")
        self.assertEqual(actual_candidate.metadata.rdi, "Commercial")
        self.assertEqual(actual_candidate.metadata.elot_sequence, "0016")
        self.assertEqual(actual_candidate.metadata.elot_sort, "A")
        self.assertEqual(actual_candidate.metadata.latitude, 40.27658)
        self.assertEqual(actual_candidate.metadata.longitude, -111.65759)
        self.assertEqual(actual_candidate.metadata.coordinate_license, 1)
        self.assertEqual(actual_candidate.metadata.precision, "Zip9")
        self.assertEqual(actual_candidate.metadata.time_zone, "Mountain")
        self.assertEqual(actual_candidate.metadata.utc_offset, -7)
        self.assertEqual(actual_candidate.metadata.obeys_dst, True)
        self.assertEqual(actual_candidate.metadata.is_ews_match, True)
        self.assertEqual(actual_candidate.analysis.dpv_match_code, "S")
        self.assertEqual(actual_candidate.analysis.dpv_footnotes, "AACCRR")
        self.assertEqual(actual_candidate.analysis.cmra, "Y")
        self.assertEqual(actual_candidate.analysis.vacant, "N")
        self.assertEqual(actual_candidate.analysis.active, "Y")
        self.assertEqual(actual_candidate.analysis.dpv_no_stat, "N")
        self.assertEqual(actual_candidate.analysis.footnotes, "footnotes")
        self.assertEqual(actual_candidate.analysis.lacs_link_code, "lacslink_code")
        self.assertEqual(actual_candidate.analysis.lacs_link_indicator, "lacslink_indicator")
        self.assertEqual(actual_candidate.analysis.is_suite_link_match, True)
        self.assertEqual(actual_candidate.analysis.enhanced_match, "enhanced_match")
