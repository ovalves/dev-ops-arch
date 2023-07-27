import unittest
from src.core.__shared.domain.repositories.interface import (
    RepositoryInterface,
    SearchableRepositoryInterface,
)


class TestRepositoryInterface(unittest.TestCase):
    def test_throw_error_when_methods_not_implemented(self):
        with self.assertRaises(TypeError) as assert_error:
            RepositoryInterface()

        self.assertEqual(
            assert_error.exception.args[0],
            "Can't instantiate abstract class RepositoryInterface with abstract "
            + "methods delete, find_all, find_by_id, insert, update",
        )


class TestSearchableRepositoryInterface(unittest.TestCase):
    def test_throw_error_when_methods_not_implemented(self):
        with self.assertRaises(TypeError) as assert_error:
            SearchableRepositoryInterface()

        self.assertEqual(
            "Can't instantiate abstract class SearchableRepositoryInterface with abstract "
            + "methods delete, find_all, find_by_id, insert, search, update",
            assert_error.exception.args[0],
        )

    def test_sortable_fields_prop(self):
        self.assertEqual(SearchableRepositoryInterface.sortable_fields, [])
