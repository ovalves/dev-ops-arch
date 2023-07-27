import abc
from abc import ABC
from typing import Generic, List
from dataclasses import dataclass, field
from src.core.__shared.domain.repositories.interface import (
    RepositoryInterface,
    SearchableRepositoryInterface,
)
from src.core.__shared.domain.value_objects import UniqueEntityId
from src.core.__shared.domain.types import ENTITY, Filter
from src.core.__shared.domain.exceptions import NotFoundException

from src.core.__shared.domain.repositories.search import SearchParams, SearchResult


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
        if item := self._get(str(entity_id)):
            self.items.remove(item)

    def _get(self, entity_id: str) -> ENTITY:
        if entity := next(
            filter(lambda entry: entry.id == entity_id, self.items), None
        ):
            return entity

        raise NotFoundException(f"Entity not found using ID '{entity_id}'")


class InMemorySearchableRepository(
    Generic[ENTITY, Filter],
    InMemoryRepository[ENTITY],
    SearchableRepositoryInterface[
        ENTITY, SearchParams[Filter], SearchResult[ENTITY, Filter]
    ],
    ABC,
):
    def search(
        self, input_params: SearchParams[Filter]
    ) -> SearchResult[ENTITY, Filter]:
        items_filtered = self._apply_filter(self.items, input_params.filter)
        items_sorted = self._apply_sort(
            items_filtered, input_params.sort, input_params.sort_dir
        )
        items_paginated = self._apply_paginate(
            items_sorted, input_params.page, input_params.per_page
        )

        return SearchResult(
            items=items_paginated,
            total=len(items_filtered),
            current_page=input_params.page,
            per_page=input_params.per_page,
            sort=input_params.sort,
            sort_dir=input_params.sort_dir,
            filter=input_params.filter,
        )

    @abc.abstractmethod
    def _apply_filter(
        self, items: List[ENTITY], filter_param: Filter | None
    ) -> List[ENTITY]:
        raise NotImplementedError()

    def _apply_sort(
        self, items: List[ENTITY], sort: str | None, sort_dir: str | None
    ) -> List[ENTITY]:
        if sort and sort in self.sortable_fields:
            is_reverse = sort_dir == "desc"
            return sorted(
                items, key=lambda item: getattr(item, sort), reverse=is_reverse
            )
        return items

    def _apply_paginate(
        self, items: List[ENTITY], page: int, per_page: int
    ) -> List[ENTITY]:  # pylint: disable=no-self-use
        start = (page - 1) * per_page
        limit = start + per_page
        return items[slice(start, limit)]
