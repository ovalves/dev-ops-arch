import abc
from abc import ABC
from dataclasses import dataclass, field
import math
from typing import Any, Generic, List, Optional, TypeVar

from src.__shared.domain.repositories.interface import RepositoryInterface
from src.__shared.domain.value_objects import UniqueEntityId
from src.__shared.domain.entities import Entity
from src.__shared.domain.types import ENTITY
from src.__shared.domain.exceptions import NotFoundException


@dataclass(slots=True)
class InMemoryRepository(RepositoryInterface[ENTITY], ABC):
    items: List[ENTITY] = field(default_factory=lambda: [])

    def insert(self, entity: ENTITY) -> None:
        self.items.append(entity)

    def bulk_insert(self, entities: List[ENTITY]) -> None:
        self.items = entities + self.items

    def find_by_id(self, entity_id: str | UniqueEntityId) -> ENTITY:
        return self._get(str(entity_id))

    def find_all(self) -> List[ENTITY]:
        return self.items

    def update(self, entity: ENTITY) -> None:
        entity_found = self._get(entity.id)
        index = self.items.index(entity_found)
        self.items[index] = entity

    def delete(self, entity_id: str | UniqueEntityId) -> None:
        entity_found = str(entity_id)
        self.items.remove(entity_found)

    def _get(self, entity_id: str) -> ENTITY:
        if entity := next(
            filter(lambda entry: entry.id == entity_id, self.items), None
        ):
            return entity

        raise NotFoundException(f"Entity not found using ID '{entity_id}'")
