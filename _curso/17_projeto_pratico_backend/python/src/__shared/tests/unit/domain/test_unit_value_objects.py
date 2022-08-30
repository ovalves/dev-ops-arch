import unittest
import uuid
from unittest.mock import patch
from dataclasses import is_dataclass
from __shared.domain.value_objects import UniqueEntityId
from __shared.domain.exceptions import InvalidUuidException

class TestUniqueEntityIdUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_entity_validate_should_called_once(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            UniqueEntityId('97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5')
            mock_validate.assert_called_once()

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ):
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId('fake id')
            self.assertEqual(assert_error.exception.args[0], 'ID must be a valid UUID')

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ):
            value_object = UniqueEntityId('97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5')
            self.assertEqual(value_object.id, '97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5')

    def test_uuid_should_be_a_string(self):
        uuid_value = uuid.uuid4()
        value_object = UniqueEntityId(uuid_value)
        self.assertEqual(value_object.id, str(uuid_value))