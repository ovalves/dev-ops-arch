from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, List, TypeVar

Item = TypeVar("Item")


@dataclass(frozen=True, slots=True)
class PaginationOutput(Generic[Item]):
    items: List[Item]
    total: int
    current_page: int
    per_page: int
    last_page: int
