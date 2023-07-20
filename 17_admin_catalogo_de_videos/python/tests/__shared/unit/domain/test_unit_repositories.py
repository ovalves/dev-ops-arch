# pylint: disable=unexpected-keyword-arg

from dataclasses import dataclass
from typing import List, Optional
import unittest
from src.__shared.domain.entities import Entity
from src.__shared.domain.types import ENTITY
from src.__shared.domain.repositories.interface import RepositoryInterface
from src.__shared.domain.repositories.memory import InMemoryRepository
from src.__shared.domain.exceptions import NotFoundException
from src.__shared.domain.value_objects import UniqueEntityId


class TestRepositoryInterface(unittest.TestCase):
    def test_throw_error_when_methods_not_implemented(self):
        with self.assertRaises(TypeError) as assert_error:
            RepositoryInterface()

        self.assertEqual(
            assert_error.exception.args[0],
            "Can't instantiate abstract class RepositoryInterface with abstract "
            + "methods delete, find_all, find_by_id, insert, update",
        )


@dataclass(frozen=True, kw_only=True, slots=True)
class StubEntity(Entity):
    name: str
    price: float


class StubInMemoryRepository(InMemoryRepository[StubEntity]):
    pass


class TestInMemoryRepository(unittest.TestCase):
    repo: StubInMemoryRepository

    def setUp(self) -> None:
        self.repo = StubInMemoryRepository()

    def test_items_prop_is_empty_on_init(self):
        self.assertEqual(self.repo.items, [])

    def test_insert(self):
        entity = StubEntity(name="test", price=5)
        self.repo.insert(entity)
        self.assertEqual(self.repo.items[0], entity)

    def test_throw_not_found_exception_in_find_by_id(self):
        with self.assertRaises(NotFoundException) as assert_error:
            self.repo.find_by_id("fake id")

        self.assertEqual(
            assert_error.exception.args[0], "Entity not found using ID 'fake id'"
        )

        unique_entity_id = UniqueEntityId("af46842e-027d-4c91-b259-3a3642144ba4")
        with self.assertRaises(NotFoundException) as assert_error:
            self.repo.find_by_id(unique_entity_id)

        self.assertEqual(
            assert_error.exception.args[0],
            "Entity not found using ID 'af46842e-027d-4c91-b259-3a3642144ba4'",
        )

    def test_find_by_id(self):
        entity = StubEntity(name="test", price=5)
        self.repo.insert(entity)

        entity_found = self.repo.find_by_id(entity.id)
        self.assertEqual(entity_found, entity)

        entity_found = self.repo.find_by_id(entity.unique_entity_id)
        self.assertEqual(entity_found, entity)

    def test_find_all(self):
        entity = StubEntity(name="test", price=5)
        self.repo.insert(entity)

        items = self.repo.find_all()
        self.assertListEqual(items, [entity])
