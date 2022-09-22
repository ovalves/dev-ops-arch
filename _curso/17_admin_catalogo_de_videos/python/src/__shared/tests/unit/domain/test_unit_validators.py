import unittest
from dataclasses import fields
from __shared.domain.exceptions import ValidationException
from __shared.domain.validators import ValidatorRules


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
