from dataclasses import dataclass
from src.__shared.application.usecases import UseCase
from src.category.domain.repositories import CategoryRepository


@dataclass(slots=True, frozen=True)
class DeleteCategoryUseCase(UseCase):
    category_repo: CategoryRepository

    def execute(self, input_param: "Input") -> None:
        self.category_repo.delete(input_param.id)

    @dataclass(slots=True, frozen=True)
    class Input:
        id: str
