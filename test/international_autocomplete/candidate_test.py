import unittest

from smartystreets_python_sdk.international_autocomplete import Candidate


class TestSuggestion(unittest.TestCase):
    def test_all_fields_get_filled_in_correctly(self):
        response_dictionary = {"street": "1", "locality": "2", "administrative_area": "3", "postal_code": "4", "country_iso3": "5"}

        suggestion = Candidate(response_dictionary)

        self.assertIsNotNone(suggestion)
        self.assertEqual('1', suggestion.street)
        self.assertEqual('2', suggestion.locality)
        self.assertEqual('3', suggestion.administrative_area)
        self.assertEqual('4', suggestion.postal_code)
        self.assertEqual('5', suggestion.country_iso3)
