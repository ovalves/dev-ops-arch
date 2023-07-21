from dataclasses import dataclass
from typing import Generic, Optional
from src.__shared.domain.types import Filter


@dataclass(frozen=True, slots=True)
class SearchInput(Generic[Filter]):
    page: Optional[int] = None
    per_page: Optional[int] = None
    sort: Optional[str] = None
    sort_dir: Optional[str] = None
    filter: Optional[Filter] = None
