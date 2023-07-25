from dataclasses import asdict, dataclass
from src.__shared.application.usecases import UseCase
from src.__shared.application.dto.search_input import SearchInput
from src.__shared.application.dto.pagination_output import PaginationOutput
from src.__shared.application.mapper.pagination_output_mapper import (
    PaginationOutputMapper,
)
from src.category.domain.repositories import CategoryRepository
from src.category.application.dto.category_output import CategoryOutput
from src.category.application.mapper.category_output_mapper import CategoryOutputMapper


@dataclass(slots=True, frozen=True)
class ListCategoriesUseCase(UseCase):
    category_repo: CategoryRepository

    def execute(self, input_param: "Input") -> "Output":
        search_params = self.category_repo.SearchParams(**asdict(input_param))
        result = self.category_repo.search(search_params)
        return self.__to_output(result)

    def __to_output(self, result: CategoryRepository.SearchResult):
        items = list(map(CategoryOutputMapper.without_child().to_output, result.items))
        return PaginationOutputMapper.from_child(
            ListCategoriesUseCase.Output
        ).to_output(items, result)

    @dataclass(slots=True, frozen=True)
    class Input(SearchInput[str]):
        pass

    @dataclass(slots=True, frozen=True)
    class Output(PaginationOutput[CategoryOutput]):
        pass
