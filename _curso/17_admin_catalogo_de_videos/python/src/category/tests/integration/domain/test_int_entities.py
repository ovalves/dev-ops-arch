# pylint: disable=unexpected-keyword-arg
import unittest
from category.domain.entities import Category
from __shared.domain.exceptions import EntityValidationException


class TestCategoryIntegration(unittest.TestCase):
    def test_create_with_invalid_cases_for_name_prop(self):
        pass
