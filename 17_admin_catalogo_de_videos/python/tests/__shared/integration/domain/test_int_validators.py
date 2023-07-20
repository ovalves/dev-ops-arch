import unittest
from rest_framework import serializers
from src.__shared.domain.validators.drf_validator_adapter import DRFValidatorAdapter


# pylint: disable=abstract-method
class StubSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()


class TestDRFValidatorIntegration(unittest.TestCase):
    def test_validation_with_error(self):
        validator = DRFValidatorAdapter()
        serializer = StubSerializer(data={})
        is_valid = validator.validate(serializer)
        self.assertFalse(is_valid)
        self.assertDictEqual(
            validator.errors,
            {"name": ["This field is required."], "price": ["This field is required."]},
        )

    def test_validate_without_error(self):
        validator = DRFValidatorAdapter()
        serializer = StubSerializer(data={"name": "some value", "price": 5})
        is_valid = validator.validate(serializer)
        self.assertTrue(is_valid)
        self.assertDictEqual(
            validator.validated_data, {"name": "some value", "price": 5}
        )
