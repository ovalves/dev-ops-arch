import unittest
from dataclasses import fields
from unittest.mock import MagicMock, PropertyMock, patch
from rest_framework import serializers
from src.__shared.domain.exceptions import ValidationException
from src.__shared.domain.validators.drf_validator_adapter import (
    DRFValidatorAdapter,
    DRFStrictBooleanField,
    DRFStrictCharField,
    ValidatorFieldsInterface,
)
from src.__shared.domain.validators.custom_validator_adapter import (
    CustomValidatorAdapter,
)


class StubStrictCharFieldSerializer(serializers.Serializer):
    name = DRFStrictCharField()


class StubStrictCharFieldSerializerWithParams(serializers.Serializer):
    name = DRFStrictCharField(required=False, allow_null=True)


class StubStrictBooleanFieldSerializer(serializers.Serializer):
    active = DRFStrictBooleanField()


class StubStrictBooleanFieldSerializerWithParams(serializers.Serializer):
    name = DRFStrictBooleanField(allow_null=True)


class TestValidatorFieldsInterfaceUnit(unittest.TestCase):
    def test_throw_error_when_validate_method_not_implemented(self):
        with self.assertRaises(TypeError) as context:
            ValidatorFieldsInterface()  # pylint: disable=abstract-class-instantiated

        self.assertEqual(
            str(context.exception),
            "Can't instantiate abstract class ValidatorFieldsInterface "
            + "with abstract method validate",
        )

    def test_validator_fields(self):
        fields_class = fields(ValidatorFieldsInterface)
        self.__validate_fields_is_none(fields_class, field_index=0, field_name="errors")
        self.__validate_fields_is_none(
            fields_class, field_index=1, field_name="validated_data"
        )

    def __validate_fields_is_none(self, fields_class, field_index, field_name):
        errors_field = fields_class[field_index]
        self.assertEqual(errors_field.name, field_name)
        self.assertIsNone(errors_field.default)


class TestDRFValidatorAdapterUnit(unittest.TestCase):
    @patch.object(serializers.Serializer, "is_valid", return_value=True)
    @patch.object(
        serializers.Serializer,
        "validated_data",
        return_value={"field": "value"},
        new_callable=PropertyMock,
    )
    def test_if_validated_data_is_set(
        self, mock_validated_data: PropertyMock, mock_is_valid: MagicMock
    ):
        validator = DRFValidatorAdapter()
        is_valid = validator.validate(serializers.Serializer())
        self.assertTrue(is_valid)
        self.assertEqual(validator.validated_data, {"field": "value"})
        mock_validated_data.assert_called()
        mock_is_valid.assert_called()

    @patch.object(serializers.Serializer, "is_valid", return_value=False)
    @patch.object(
        serializers.Serializer,
        "errors",
        return_value={"field": ["some error"]},
        new_callable=PropertyMock,
    )
    def test_if_errors_is_set(
        self, mock_errors: PropertyMock, mock_is_valid: MagicMock
    ):
        validator = DRFValidatorAdapter()
        is_valid = validator.validate(serializers.Serializer())
        self.assertFalse(is_valid)
        self.assertEqual(validator.errors, {"field": ["some error"]})
        mock_errors.assert_called()
        mock_is_valid.assert_called()


class TestStrictCharFieldUnit(unittest.TestCase):
    def test_if_is_invalid_when_not_str_values(self):
        serializer = StubStrictCharFieldSerializer(data={"name": 5})
        serializer.is_valid()
        self.assertEqual(
            serializer.errors,
            {
                "name": [
                    serializers.ErrorDetail(
                        string="Not a valid string.", code="invalid"
                    )
                ]
            },
        )

        serializer = StubStrictCharFieldSerializer(data={"name": True})
        serializer.is_valid()
        self.assertEqual(
            serializer.errors,
            {
                "name": [
                    serializers.ErrorDetail(
                        string="Not a valid string.", code="invalid"
                    )
                ]
            },
        )

    def test_none_value_is_valid(self):
        serializer = StubStrictCharFieldSerializerWithParams(data={"name": None})
        self.assertTrue(serializer.is_valid())

    def test_is_valid(self):
        serializer = StubStrictCharFieldSerializer(data={"name": "some value"})
        self.assertTrue(serializer.is_valid())


class TestStrictBooleanFieldUnit(unittest.TestCase):
    def test_if_is_invalid_when_not_bool_values(self):
        message_error = "Must be a valid boolean."

        serializer = StubStrictBooleanFieldSerializer(data={"active": 0})
        serializer.is_valid()
        self.assertEqual(
            serializer.errors,
            {"active": [serializers.ErrorDetail(string=message_error, code="invalid")]},
        )

        serializer = StubStrictBooleanFieldSerializer(data={"active": 1})
        serializer.is_valid()
        self.assertEqual(
            serializer.errors,
            {"active": [serializers.ErrorDetail(string=message_error, code="invalid")]},
        )

        serializer = StubStrictBooleanFieldSerializer(data={"active": "True"})
        serializer.is_valid()
        self.assertEqual(
            serializer.errors,
            {"active": [serializers.ErrorDetail(string=message_error, code="invalid")]},
        )

        serializer = StubStrictBooleanFieldSerializer(data={"active": "False"})
        serializer.is_valid()
        self.assertEqual(
            serializer.errors,
            {"active": [serializers.ErrorDetail(string=message_error, code="invalid")]},
        )

    def test_is_valid(self):
        serializer = StubStrictBooleanFieldSerializerWithParams(data={"name": None})
        self.assertTrue(serializer.is_valid())

        serializer = StubStrictBooleanFieldSerializerWithParams(data={"name": True})
        self.assertTrue(serializer.is_valid())

        serializer = StubStrictBooleanFieldSerializerWithParams(data={"name": False})
        self.assertTrue(serializer.is_valid())
