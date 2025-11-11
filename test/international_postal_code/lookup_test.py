import unittest
from smartystreets_python_sdk.international_postal_code.lookup import Lookup

class TestLookupSerialization(unittest.TestCase):
    def test_nothing_to_serialize(self):
        l = Lookup()
        params = {}
        l.populate(params)
        self.assertEqual(params, {})

    def test_full_lookup(self):
        l = Lookup()
        l.input_id = "Hello, World!"
        l.country = "CAN"
        l.locality = "Toronto"
        l.administrative_area = "ON"
        l.postal_code = "ABC DEF"
        params = {}
        l.populate(params)
        self.assertEqual(params['input_id'], "Hello, World!")
        self.assertEqual(params['country'], "CAN")
        self.assertEqual(params['locality'], "Toronto")
        self.assertEqual(params['administrative_area'], "ON")
        self.assertEqual(params['postal_code'], "ABC DEF")


if __name__ == "__main__":
    unittest.main()
