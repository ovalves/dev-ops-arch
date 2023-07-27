from dataclasses import dataclass
from typing import Optional
from src.core.__shared.application.usecases import UseCase
from src.core.category.domain.entities.category import Category
from src.core.category.domain.repositories import CategoryRepository
from src.core.category.application.dto.category_output import CategoryOutput
from src.core.category.application.mapper.category_output_mapper import (
    CategoryOutputMapper,
)


@dataclass(slots=True, frozen=True)
class UpdateCategoryUseCase(UseCase):
    category_repo: CategoryRepository

    def execute(self, input_param: "Input") -> "Output":
        entity = self.category_repo.find_by_id(input_param.id)
        entity.update(input_param.name, input_param.description)

        if input_param.is_active is True:
            entity.activate()

        if input_param.is_active is False:
            entity.deactivate()

        self.category_repo.update(entity)
        return self.__to_output(entity)

    def __to_output(self, category: Category) -> "Output":
        return CategoryOutputMapper.from_child(UpdateCategoryUseCase.Output).to_output(
            category
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        id: str
        name: str
        description: Optional[str] = Category.get_field("description").default
        is_active: Optional[bool] = Category.get_field("is_active").default

    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass
