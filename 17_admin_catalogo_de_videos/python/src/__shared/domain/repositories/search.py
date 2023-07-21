import math
from dataclasses import dataclass, field
from typing import Any, Generic, List, Optional
from src.__shared.domain.types import ENTITY, Filter


@dataclass(slots=True, kw_only=True)
class SearchParams(Generic[Filter]):
    page: Optional[int] = 1
    per_page: Optional[int] = 20
    sort: Optional[str] = None
    sort_dir: Optional[str] = None
    filter: Optional[Filter] = None

    def __post_init__(self):
        self._normalize_page()
        self._normalize_per_page()
        self._normalize_sort()
        self._normalize_sort_dir()
        self._normalize_filter()

    def _normalize_page(self):
        page = self._convert_to_int(self.page)
        if page <= 0:
            page = self._get_dataclass_field("page").default
        self.page = page

    def _normalize_per_page(self):
        per_page = self._convert_to_int(self.per_page)
        if per_page < 1:
            per_page = self._get_dataclass_field("per_page").default
        self.per_page = per_page

    def _normalize_sort(self):
        self.sort = None if self.sort == "" or self.sort is None else str(self.sort)

    def _normalize_sort_dir(self):
        if not self.sort:
            self.sort_dir = None
            return

        sort_dir = str(self.sort_dir).lower()
        self.sort_dir = "asc" if sort_dir not in ["asc", "desc"] else sort_dir

    def _normalize_filter(self):
        self.filter = (
            None if self.filter == "" or self.filter is None else str(self.filter)
        )

    def _convert_to_int(self, value: Any, default=0) -> int:
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    def _get_dataclass_field(self, field_name):
        return SearchParams.__dataclass_fields__[field_name]


@dataclass(slots=True, kw_only=True, frozen=True)
class SearchResult(Generic[ENTITY, Filter]):
    items: List[ENTITY]
    total: int
    current_page: int
    per_page: int
    last_page: int = field(init=False)
    sort: Optional[str] = None
    sort_dir: Optional[str] = None
    filter: Optional[Filter] = None

    def __post_init__(self):
        object.__setattr__(self, "last_page", math.ceil(self.total / self.per_page))

    def to_dict(self):
        return {
            "items": self.items,
            "total": self.total,
            "current_page": self.current_page,
            "per_page": self.per_page,
            "last_page": self.last_page,
            "sort": self.sort,
            "sort_dir": self.sort_dir,
            "filter": self.filter,
        }
