import unittest
from unittest.mock import patch

from src.__shared.domain.exceptions import NotFoundException
from src.__shared.application.usecases import UseCase
from src.category.application.dto.category_output import CategoryOutput
from src.category.domain.entities.category import Category
from src.category.infra.repositories.in_memory import CategoryInMemoryRepository
from src.category.application.usecases.get_category_usecase import (
    GetCategoryUseCase,
)


class TestCreateCategoryUseCaseUnit(unittest.TestCase):
    use_case: GetCategoryUseCase
    category_repo: CategoryInMemoryRepository

    def setUp(self) -> None:
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = GetCategoryUseCase(self.category_repo)

    def test_if_instance_a_use_case(self):
        self.assertIsInstance(self.use_case, UseCase)

    def test_input(self):
        self.assertEqual(GetCategoryUseCase.Input.__annotations__, {"id": str})

    def test_output(self):
        self.assertTrue(issubclass(GetCategoryUseCase.Output, CategoryOutput))

    def test_throws_exception_when_category_not_found(self):
        input_param = GetCategoryUseCase.Input("fake id")
        with self.assertRaises(NotFoundException) as assert_error:
            self.use_case.execute(input_param)
        self.assertEqual(
            assert_error.exception.args[0], "Entity not found using ID 'fake id'"
        )

    def test_execute(self):
        category = Category(name="Movie")
        self.category_repo.insert(category)

        with patch.object(
            self.category_repo, "find_by_id", wraps=self.category_repo.find_by_id
        ) as spy_find_by_id:
            input_param = GetCategoryUseCase.Input(category.id)
            output = self.use_case.execute(input_param)
            spy_find_by_id.assert_called_once()
            self.assertEqual(
                output,
                GetCategoryUseCase.Output(
                    id=self.category_repo.items[0].id,
                    name="Movie",
                    description=None,
                    is_active=True,
                    created_at=self.category_repo.items[0].created_at,
                ),
            )
