import unittest
from src.category.domain.entities.category import CustomCategoryRules, Category
from src.category.domain.factory.category_validator_factory import (
    CategoryValidatorFactory,
)


class TestCustomCategoryValidatorUnit(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = CategoryValidatorFactory.create(CustomCategoryRules)
        return super().setUp()

    def test_with_custom_validator(self):
        invalid_data = [
            {"data": {"name": None}, "expected": "This field may not be null."},
            {"data": {"name": ""}, "expected": "This field may not be blank."},
            {"data": {"name": "5"}, "expected": "Not a valid string."},
            {
                "data": {"name": "a" * 256},
                "expected": "Ensure this field has no more than 255 characters.",
            },
        ]

        for i in invalid_data:
            is_valid = self.validator.validate(i["data"])
            self.assertFalse(is_valid)

    def test_validate_category_fields(self):
        category = Category(name="Movie")
        is_valid = self.validator.validate(category.to_dict())
        self.assertTrue(is_valid)
