import unittest

from smartystreets_python_sdk import NativeSerializer
from smartystreets_python_sdk.us_extract import Result


class TestResult(unittest.TestCase):
    def test_all_fields_filled_correctly(self):
        deserializer = NativeSerializer()
        response_payload = '{"meta":{"lines":1,"unicode":true,"address_count":2,'\
            '"verified_count":3,"bytes":4,"character_count":5},"addresses":[{"text":"6",'\
            '"verified":true,"line":7,"start":8,"end":9,"api_output":[{}]},{"text":"10"}]}'
        obj = deserializer.deserialize(response_payload)
        result = Result(obj)

        metadata = result.metadata
        self.assertIsNotNone(metadata)
        self.assertEqual(1, metadata.lines)
        self.assertEqual(True, metadata.unicode)
        self.assertEqual(2, metadata.address_count)
        self.assertEqual(3, metadata.verified_count)
        self.assertEqual(4, metadata.bytes)
        self.assertEqual(5, metadata.character_count)

        address = result.addresses[0]
        self.assertIsNotNone(address)
        self.assertEqual('6', address.text)
        self.assertEqual(True, address.verified)
        self.assertEqual(7, address.line)
        self.assertEqual(8, address.start)
        self.assertEqual(9, address.end)
        self.assertEqual('10', result.addresses[1].text)

        candidates = address.candidates
        self.assertIsNotNone(candidates)
