import abc
from abc import ABC
from typing import Any, Generic, List, Optional, TypeVar

from src.core.__shared.domain.value_objects import UniqueEntityId
from src.core.__shared.domain.types import ENTITY, Input, Output


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


class SearchableRepositoryInterface(
    Generic[ENTITY, Input, Output], RepositoryInterface[ENTITY], ABC
):
    sortable_fields: List[str] = []

    @abc.abstractmethod
    def search(self, input_params: Input) -> Output:
        raise NotImplementedError()
