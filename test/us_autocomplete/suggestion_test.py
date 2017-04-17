import unittest

from smartystreets_python_sdk.us_autocomplete import Suggestion


class TestSuggestion(unittest.TestCase):
    def test_all_fields_get_filled_in_correctly(self):
        response_dictionary = {"text": "1", "street_line": "2", "city": "3", "state": "4"}

        suggestion = Suggestion(response_dictionary)

        self.assertIsNotNone(suggestion)
        self.assertEqual('1', suggestion.text)
        self.assertEqual('2', suggestion.street_line)
        self.assertEqual('3', suggestion.city)
        self.assertEqual('4', suggestion.state)
