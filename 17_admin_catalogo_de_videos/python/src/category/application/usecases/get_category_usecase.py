from dataclasses import dataclass
from src.__shared.application.usecases import UseCase
from src.category.domain.entities.category import Category
from src.category.domain.repositories import CategoryRepository
from src.category.application.dto.category_output import CategoryOutput
from src.category.application.mapper.category_output_mapper import CategoryOutputMapper


@dataclass(slots=True, frozen=True)
class GetCategoryUseCase(UseCase):
    category_repo: CategoryRepository

    def execute(self, input_param: "Input") -> "Output":
        category = self.category_repo.find_by_id(input_param.id)
        return self.__to_output(category)

    def __to_output(self, category: Category):
        return CategoryOutputMapper.from_child(GetCategoryUseCase.Output).to_output(
            category
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        id: str

    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass
