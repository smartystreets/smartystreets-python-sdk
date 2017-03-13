import unittest
from smartystreets_python_sdk import Batch, us_street
from smartystreets_python_sdk.exceptions import BatchFullError


class TestBatch(unittest.TestCase):
    def setUp(self):
        self.batch = Batch()

    def test_gets_lookup_by_input_id(self):
        lookup = us_street.Lookup()
        lookup.input_id = "has input id"

        self.batch.add(lookup)

        self.assertEqual(lookup, self.batch.get_by_input_id('has input id'))

    def test_gets_lookup_by_index(self):
        lookup = us_street.Lookup()

        self.batch.add(lookup)

        self.assertEqual(lookup, self.batch[0])

    def test_returns_correct_size(self):
        self.batch.add(us_street.Lookup())
        self.batch.add(us_street.Lookup())
        self.batch.add(us_street.Lookup())

        self.assertEqual(3, len(self.batch))

    def test_clear_method_clears_both_lookup_collections(self):
        lookup = us_street.Lookup()
        lookup.input_id = "test"
        self.batch.add(lookup)

        self.batch.clear()

        self.assertEqual(0, len(self.batch.all_lookups))
        self.assertEqual(0, len(self.batch.named_lookups))

    def test_adding_a_lookup_when_batch_is_full_raises_exception(self):
        lookup = us_street.Lookup()

        for i in range(0, Batch.MAX_BATCH_SIZE):
            self.batch.add(lookup)

        self.assertRaises(BatchFullError, self.batch.add, lookup)
