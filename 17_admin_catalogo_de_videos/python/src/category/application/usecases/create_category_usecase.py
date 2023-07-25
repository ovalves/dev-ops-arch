from typing import Optional
from dataclasses import dataclass
from src.__shared.application.usecases import UseCase
from src.category.domain.entities.category import Category
from src.category.domain.repositories import CategoryRepository
from src.category.application.dto.category_output import CategoryOutput
from src.category.application.mapper.category_output_mapper import CategoryOutputMapper


@dataclass(slots=True, frozen=True)
class CreateCategoryUseCase(UseCase):
    category_repo: CategoryRepository

    def execute(self, input_param: "Input") -> "Output":
        category = Category(
            name=input_param.name,
            description=input_param.description,
            is_active=input_param.is_active,
        )
        self.category_repo.insert(category)
        return self.__to_output(category)

    def __to_output(self, category: Category):
        return CategoryOutputMapper.from_child(CreateCategoryUseCase.Output).to_output(
            category
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        name: str
        description: Optional[str] = Category.get_field("description").default
        is_active: Optional[bool] = Category.get_field("is_active").default

    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass
