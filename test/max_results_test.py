import unittest

from smartystreets_python_sdk.exceptions import UnprocessableEntityError
from smartystreets_python_sdk.max_results import normalize_max_results


class TestMaxResults(unittest.TestCase):
    def test_whole_numbers_are_converted_and_sent(self):
        self.assertEqual(5, normalize_max_results(5))
        self.assertEqual(5, normalize_max_results('5'))
        self.assertEqual(7, normalize_max_results(' 7 '))
        self.assertEqual(5, normalize_max_results(5.0))
        self.assertEqual(3, normalize_max_results('+3'))
        self.assertEqual(1000, normalize_max_results(1000))

    def test_unset_and_values_not_above_zero_are_not_sent(self):
        for value in [None, '', '  ', 0, '0', -1, '-2']:
            self.assertIsNone(normalize_max_results(value), 'expected %r to not be sent' % (value,))

    def test_values_that_are_not_whole_numbers_raise(self):
        for value in ['abc', '1.5', 1.5, True]:
            with self.assertRaises(UnprocessableEntityError, msg='expected %r to raise' % (value,)):
                normalize_max_results(value)
