# pylint: disable=unexpected-keyword-arg

from abc import ABC
from dataclasses import dataclass, is_dataclass
import unittest
from __shared.domain.entities import Entity
from __shared.domain.value_objects import UniqueEntityId


@dataclass(frozen=True)
class StubEntity(Entity):
    prop1: str = None
    prop2: str = None


class TestEntityUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(Entity(), ABC)

    def test_set_unique_entity_id_and_props(self):
        entity = StubEntity(prop1="value1", prop2="value2")
        self.assertEqual(entity.prop1, "value1")
        self.assertEqual(entity.prop2, "value2")
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)
        self.assertEqual(entity.unique_entity_id.id, entity.id)

    def test_accept_a_valid_uuid(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId("97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5"),
            prop1="value1",
            prop2="value2",
        )

        self.assertEqual(entity.id, "97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5")

    def test_convert_entity_to_dict(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId("97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5"),
            prop1="value1",
            prop2="value2",
        )
        self.assertDictEqual(
            entity.to_dict(),
            {
                "id": "97eea803-f57b-4ae9-a0cf-b5a8c6ca98f5",
                "prop1": "value1",
                "prop2": "value2",
            },
        )

    def test_set_method(self):
        entity = StubEntity(
            prop1="value1",
            prop2="value2",
        )
        # pylint: disable=protected-access
        entity._set("prop1", "changed")
        self.assertEqual(entity.prop1, "changed")
