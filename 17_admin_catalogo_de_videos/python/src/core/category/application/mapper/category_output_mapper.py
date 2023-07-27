from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from src.core.__shared.domain.types import CategoryOutputType
from src.core.category.application.dto.category_output import CategoryOutput
from src.core.category.domain.entities.category import Category


@dataclass(frozen=True, slots=True)
class CategoryOutputMapper:
    output_child: Optional[CategoryOutputType] = CategoryOutput

    @staticmethod
    def from_child(output_child: CategoryOutputType):
        return CategoryOutputMapper(output_child)

    @staticmethod
    def without_child():
        return CategoryOutputMapper()

    def to_output(self, category: Category) -> CategoryOutput:
        return self.output_child(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
            created_at=category.created_at,
        )
