import unittest

from smartystreets_python_sdk.exceptions import UnprocessableEntityError
from smartystreets_python_sdk.international_street import LanguageMode


class TestLanguageMode(unittest.TestCase):
    def test_from_value_resolves_mixed_case(self):
        self.assertEqual(LanguageMode.LATIN, LanguageMode.from_value('Latin'))
        self.assertEqual(LanguageMode.NATIVE, LanguageMode.from_value('NATIVE'))
        self.assertEqual(LanguageMode.LATIN, LanguageMode.from_value('latin'))

    def test_from_value_returns_language_mode_instance_unchanged(self):
        self.assertEqual(LanguageMode.NATIVE, LanguageMode.from_value(LanguageMode.NATIVE))

    def test_from_value_rejects_invalid_value(self):
        self.assertRaises(UnprocessableEntityError, LanguageMode.from_value, 'Klingon')

    def test_values_are_lowercase(self):
        self.assertEqual('native', LanguageMode.NATIVE.value)
        self.assertEqual('latin', LanguageMode.LATIN.value)
