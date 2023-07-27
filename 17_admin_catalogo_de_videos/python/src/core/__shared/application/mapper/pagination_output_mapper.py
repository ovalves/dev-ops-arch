from dataclasses import dataclass
from typing import Generic, List
from src.core.__shared.domain.repositories.search import SearchResult
from src.core.__shared.domain.types import Item, Output, PaginationOutput


@dataclass(frozen=True, slots=True)
class PaginationOutputMapper:
    output_child: Output

    @staticmethod
    def from_child(output_child: Output):
        return PaginationOutputMapper(output_child)

    def to_output(self, items: List[Item], result: SearchResult) -> PaginationOutput:
        return self.output_child(
            items=items,
            total=result.total,
            current_page=result.current_page,
            per_page=result.per_page,
            last_page=result.last_page,
        )
