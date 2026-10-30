import unittest
from smartystreets_python_sdk.international_postal_code.lookup import Lookup
from smartystreets_python_sdk.international_postal_code.language_mode import LanguageMode

class TestLookupSerialization(unittest.TestCase):
    def test_nothing_to_serialize(self):
        l = Lookup()
        params = {}
        l.populate(params)
        self.assertEqual(params, {})

    def test_language_blank(self):
        l = Lookup()
        l.language = None
        params = {}
        l.populate(params)
        self.assertEqual(params, {})

    def test_language_latin(self):
        l = Lookup()
        l.language = LanguageMode.LATIN
        params = {}
        l.populate(params)
        self.assertEqual(params, {'language': 'latin'})

    def test_language_native(self):
        l = Lookup()
        l.language = LanguageMode.NATIVE
        params = {}
        l.populate(params)
        self.assertEqual(params, {'language': 'native'})

    def test_language_mixed_case(self):
        l = Lookup()
        l.language = 'NATIVE'
        params = {}
        l.populate(params)
        self.assertEqual(params, {'language': 'native'})

    def test_max_results_unset(self):
        l = Lookup()
        l.max_results = 0
        params = {}
        l.populate(params)
        self.assertEqual(params, {})

    def test_max_results(self):
        l = Lookup()
        l.max_results = 1000
        params = {}
        l.populate(params)
        self.assertEqual(params, {'max_results': 1000})

    def test_full_lookup(self):
        l = Lookup()
        l.input_id = "Hello, World!"
        l.country = "CAN"
        l.language = LanguageMode.NATIVE
        l.locality = "Toronto"
        l.administrative_area = "ON"
        l.postal_code = "ABC DEF"
        l.max_results = 25
        params = {}
        l.populate(params)
        self.assertEqual(params['input_id'], "Hello, World!")
        self.assertEqual(len(params), 7)
        self.assertEqual(params['country'], "CAN")
        self.assertEqual(params['language'], "native")
        self.assertEqual(params['locality'], "Toronto")
        self.assertEqual(params['administrative_area'], "ON")
        self.assertEqual(params['postal_code'], "ABC DEF")
        self.assertEqual(params['max_results'], 25)


if __name__ == "__main__":
    unittest.main()
