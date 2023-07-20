import unittest
from abc import ABC
from unittest.mock import patch
from dataclasses import FrozenInstanceError, dataclass, is_dataclass
from src.__shared.domain.value_objects import UniqueEntityId, ValueObject
from src.__shared.domain.exceptions import InvalidUuidException


@dataclass(frozen=True)
class StubOneProp(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProp(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        value_object_1 = StubOneProp(prop="value")
        self.assertEqual(value_object_1.prop, "value")

        value_object_2 = StubTwoProp(prop1="value1", prop2="value2")
        self.assertEqual(value_object_2.prop1, "value1")
        self.assertEqual(value_object_2.prop2, "value2")

    def test_convert_to_string(self):
        value_object_1 = StubOneProp(prop="value")
        self.assertEqual("value", str(value_object_1))

        value_object_2 = StubTwoProp(prop1="value1", prop2="value2")
        self.assertEqual('{"prop1": "value1", "prop2": "value2"}', str(value_object_2))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = StubOneProp(prop="value")
            value_object.prop = "fake"


class TestUniqueEntityIdUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_entity_validate_should_called_once(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,
        ) as mock_validate:
            UniqueEntityId("97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5")
            mock_validate.assert_called_once()

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,
        ):
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId("fake id")
            self.assertEqual(assert_error.exception.args[0], "ID must be a valid UUID")

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,
        ):
            value_object = UniqueEntityId("97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5")
            self.assertEqual(value_object.id, "97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5")

    def test_uuid_should_be_a_string(self):
        value_object = UniqueEntityId("97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5")
        self.assertIsInstance(value_object.id, str)

    def test_UniqueEntityId_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = "fake id"
