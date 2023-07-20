import abc
from abc import ABC
from dataclasses import dataclass, field
import math
from typing import Any, Generic, List, Optional, TypeVar

from __shared.domain.value_objects import UniqueEntityId
from __shared.domain.entities import Entity
from __shared.domain.types import ENTITY


class RepositoryInterface(Generic[ENTITY], ABC):
    @abc.abstractmethod
    def insert(self, entity: ENTITY) -> None:
        raise NotImplementedError()

    def bulk_insert(self, entities: List[ENTITY]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, entity_id: str | UniqueEntityId) -> ENTITY:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[ENTITY]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity: ENTITY) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, entity_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
