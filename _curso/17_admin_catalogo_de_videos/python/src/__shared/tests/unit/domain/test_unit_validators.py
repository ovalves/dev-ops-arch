import unittest
from dataclasses import fields
from unittest.mock import MagicMock, PropertyMock, patch
from rest_framework import serializers
from __shared.domain.exceptions import ValidationException
from __shared.domain.validators import (
    DRFValidator,
    StrictBooleanField,
    StrictCharField,
    ValidatorFieldsInterface,
    ValidatorRules,
)


class StubStrictCharFieldSerializer(serializers.Serializer):
    name = StrictCharField()


class StubStrictCharFieldSerializerWithParams(serializers.Serializer):
    name = StrictCharField(required=False, allow_null=True)


class StubStrictBooleanFieldSerializer(serializers.Serializer):
    active = StrictBooleanField()


class StubStrictBooleanFieldSerializerWithParams(serializers.Serializer):
    name = StrictBooleanField(allow_null=True)


class TestValidatorRulesUnit(unittest.TestCase):
    def test_values_method(self):
        validator = ValidatorRules.values("some value", "prop")
        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, "some value")
        self.assertEqual(validator.prop, "prop")

    def test_required_rule(self):

        invalid_data = [
            {"value": None, "prop": "prop"},
            {"value": "", "prop": "prop"},
        ]

        for i in invalid_data:
            msg = f'value: {i["value"]}, prop: {i["prop"]}'
            with self.assertRaises(ValidationException, msg=msg) as context:
                ValidatorRules.values(i["value"], i["prop"]).required()

            self.assertEqual("The prop is required", str(context.exception))

        valid_data = [
            {"value": "test", "prop": "prop"},
            {"value": 5, "prop": "prop"},
            {"value": 0, "prop": "prop"},
            {"value": False, "prop": "prop"},
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(i["value"], i["prop"]).required(), ValidatorRules
            )

    def test_string_rule(self):
        invalid_data = [
            {"value": 5, "prop": "prop"},
            {"value": True, "prop": "prop"},
            {"value": {}, "prop": "prop"},
        ]

        for i in invalid_data:
            msg = f'value: {i["value"]}, prop: {i["prop"]}'
            with self.assertRaises(ValidationException, msg=msg) as context:
                ValidatorRules.values(i["value"], i["prop"]).string()

            self.assertEqual(
                "The prop must be a string",
                str(context.exception),
            )

        valid_data = [
            {"value": None, "prop": "prop"},
            {"value": "", "prop": "prop"},
            {"value": "some value", "prop": "prop"},
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(i["value"], i["prop"]).string(), ValidatorRules
            )

    def test_max_length_rule(self):
        invalid_data = [
            {"value": "t" * 5, "prop": "prop"},
        ]

        for i in invalid_data:
            msg = f'value: {i["value"]}, prop: {i["prop"]}'
            with self.assertRaises(ValidationException, msg=msg) as context:
                ValidatorRules.values(i["value"], i["prop"]).max_length(4)

            self.assertEqual(
                "The prop must be less than 4 characters",
                str(context.exception),
            )

        valid_data = [
            {"value": None, "prop": "prop"},
            {"value": "t" * 5, "prop": "prop"},
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(i["value"], i["prop"]).max_length(5),
                ValidatorRules,
            )

    def test_boolean_rule(self):
        invalid_data = [
            {"value": "", "prop": "prop"},
            {"value": 5, "prop": "prop"},
            {"value": {}, "prop": "prop"},
        ]

        for i in invalid_data:
            msg = f'value: {i["value"]}, prop: {i["prop"]}'
            with self.assertRaises(ValidationException, msg=msg) as context:
                ValidatorRules.values(i["value"], i["prop"]).boolean()

            self.assertEqual(
                "The prop must be a boolean",
                str(context.exception),
            )

        valid_data = [
            {"value": None, "prop": "prop"},
            {"value": True, "prop": "prop"},
            {"value": False, "prop": "prop"},
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(i["value"], i["prop"]).boolean(), ValidatorRules
            )

    def test_throw_a_validation_exception_when_combine_two_or_more_rules(self):
        with self.assertRaises(ValidationException) as context:
            ValidatorRules.values(None, "prop").required().string().max_length(5)
        self.assertEqual(
            "The prop is required",
            str(context.exception),
        )

        with self.assertRaises(ValidationException) as context:
            ValidatorRules.values(5, "prop").required().string().max_length(5)
        self.assertEqual(
            "The prop must be a string",
            str(context.exception),
        )

        with self.assertRaises(ValidationException) as context:
            ValidatorRules.values("t" * 6, "prop").required().string().max_length(5)
        self.assertEqual(
            "The prop must be less than 5 characters",
            str(context.exception),
        )

        with self.assertRaises(ValidationException) as context:
            ValidatorRules.values(None, "prop").required().boolean()
        self.assertEqual(
            "The prop is required",
            str(context.exception),
        )

        with self.assertRaises(ValidationException) as context:
            ValidatorRules.values(5, "prop").required().boolean()
        self.assertEqual(
            "The prop must be a boolean",
            str(context.exception),
        )

    def test_valid_cases_for_combination_between_rules(self):
        ValidatorRules("test", "prop").required().string()
        ValidatorRules("t" * 5, "prop").required().string().max_length(5)

        ValidatorRules(True, "prop").required().boolean()
        ValidatorRules(False, "prop").required().boolean()
        self.assertTrue(True)


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


class TestDRFValidatorUnit(unittest.TestCase):
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
        validator = DRFValidator()
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
        validator = DRFValidator()
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
