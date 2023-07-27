import unittest
from unittest.mock import patch
from src.core.__shared.domain.exceptions import NotFoundException
from src.core.__shared.application.usecases import UseCase
from src.core.category.domain.entities.category import Category
from src.core.category.domain.repositories import CategoryRepository
from src.core.category.infra.repositories.in_memory import CategoryInMemoryRepository
from src.core.category.application.usecases.delete_category_usecase import (
    DeleteCategoryUseCase,
)


class TestDeleteCategoryUseCase(unittest.TestCase):

    use_case: DeleteCategoryUseCase
    category_repo: CategoryRepository

    def setUp(self) -> None:
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = DeleteCategoryUseCase(self.category_repo)

    def test_instance_use_case(self):
        self.assertIsInstance(self.use_case, UseCase)

    def test_input(self):
        self.assertEqual(DeleteCategoryUseCase.Input.__annotations__, {"id": str})

    def test_throw_exception_when_category_not_found(self):
        request = DeleteCategoryUseCase.Input(id="not_found")
        with self.assertRaises(NotFoundException) as assert_error:
            self.use_case.execute(request)
        self.assertEqual(
            assert_error.exception.args[0], "Entity not found using ID 'not_found'"
        )

    def test_execute(self):
        category = Category(name="test")
        self.category_repo.items = [category]
        with patch.object(
            self.category_repo, "delete", wraps=self.category_repo.delete
        ) as spy_delete:
            request = DeleteCategoryUseCase.Input(id=category.id)
            self.use_case.execute(request)
            spy_delete.assert_called_once()
            self.assertCountEqual(self.category_repo.items, [])
