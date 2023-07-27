from dataclasses import dataclass
from typing import List
from src.core.__shared.domain.repositories.memory import (
    InMemoryRepository,
    InMemorySearchableRepository,
)
from src.core.__shared.domain.entities import Entity


@dataclass(frozen=True, kw_only=True, slots=True)
class StubEntity(Entity):
    name: str
    price: float


class StubInMemorySearchableRepository(InMemorySearchableRepository[StubEntity, str]):
    sortable_fields: List[str] = ["name"]

    def _apply_filter(
        self, items: List[StubEntity], filter_param: str | None
    ) -> List[StubEntity]:
        if filter_param:
            filter_obj = filter(
                lambda i: filter_param.lower() in i.name.lower()
                or filter_param == str(i.price),
                items,
            )
            return list(filter_obj)
        return items


class StubInMemoryRepository(InMemoryRepository[StubEntity]):
    pass
