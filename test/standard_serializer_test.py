import smartystreets_python_sdk as smarty
import unittest
from smartystreets_python_sdk import us_street


class TestStandardSerializer(unittest.TestCase):

    def test_serialize(self):
        serializer = smarty.StandardSerializer()

        result = serializer.serialize([us_street.Lookup("123 fake street").__dict__])

        self.assertTrue('"street": "123 fake street"' in str(result))

    def test_deserializer(self):
        expected_json_output = "[{\"input_index\":0,\"city_states\":[{\"city\":\"Washington\",\"state_abbreviation\":\
            \"DC\",\"state\":\"District of Columbia\",\"mailable_city\":true}],\"zipcodes\":[{\"zipcode\":\"20500\",\
            \"zipcode_type\":\"S\",\"default_city\":\"Washington\",\"county_fips\":\"11001\",\
            \"county_name\":\"District of Columbia\",\"latitude\":38.89769,\"longitude\":-77.03869}]},{\"input_index\":1,\
            \"input_id\":\"test id\",\"city_states\":[{\"city\":\"Provo\",\"state_abbreviation\":\"UT\",\"state\":\"Utah\",\
            \"default_city\":true,\"mailable_city\":true}],\"zipcodes\":[{\"zipcode\":\"84606\",\"zipcode_type\":\"S\",\
            \"county_fips\":\"11501\",\"county_name\":\"Utah\",\"latitude\":38.89769,\"longitude\":-77.03869}]},\
            {\"input_index\":2,\"status\":\"invalid_zipcode\",\"reason\":\"Invalid ZIP Code.\"}]"
        serializer = smarty.StandardSerializer()

        results = serializer.deserialize(expected_json_output)

        self.assertIsNotNone(results[0])
        self.assertEqual(0, results[0]['input_index'])
        self.assertIsNotNone(results[0]['city_states'])
        self.assertEqual("Washington", results[0]['city_states'][0]['city'])
        self.assertEqual("20500", results[0]['zipcodes'][0]['zipcode'])

        self.assertIsNotNone(results[1])
        self.assertNotIn('status', results[1])
        self.assertEqual("Utah", results[1]['city_states'][0]['state'])
        self.assertEqual(38.89769, results[1]['zipcodes'][0]['latitude'], .00001)

        self.assertIsNotNone(results[2])
        self.assertNotIn('city_states', results[2])
        self.assertEqual("invalid_zipcode", results[2]['status'])
        self.assertEqual("Invalid ZIP Code.", results[2]['reason'])
