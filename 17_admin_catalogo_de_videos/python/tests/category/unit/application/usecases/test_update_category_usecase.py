from typing import Optional
import unittest
from unittest.mock import patch

from src.__shared.domain.exceptions import NotFoundException
from src.__shared.application.usecases import UseCase
from src.category.application.dto.category_output import CategoryOutput
from src.category.domain.entities.category import Category
from src.category.domain.repositories import CategoryRepository
from src.category.infra.repositories.in_memory import CategoryInMemoryRepository
from src.category.application.usecases.update_category_usecase import (
    UpdateCategoryUseCase,
)


class TestUpdateCategoryUseCase(unittest.TestCase):
    use_case: UpdateCategoryUseCase
    category_repo: CategoryRepository

    def setUp(self) -> None:
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = UpdateCategoryUseCase(self.category_repo)

    def test_instance_use_case(self):
        self.assertIsInstance(self.use_case, UseCase)

    def test_input(self):
        self.assertEqual(
            UpdateCategoryUseCase.Input.__annotations__,
            {
                "id": str,
                "name": str,
                "description": Optional[str],
                "is_active": Optional[bool],
            },
        )

        description_field = UpdateCategoryUseCase.Input.__dataclass_fields__[
            "description"
        ]
        self.assertEqual(
            description_field.default, Category.get_field("description").default
        )

        is_active_field = UpdateCategoryUseCase.Input.__dataclass_fields__["is_active"]
        self.assertEqual(
            is_active_field.default, Category.get_field("is_active").default
        )

    def test_output(self):
        self.assertTrue(issubclass(UpdateCategoryUseCase.Output, CategoryOutput))

    def test_throw_exception_when_category_not_found(self):
        request = UpdateCategoryUseCase.Input(id="not_found", name="test")
        with self.assertRaises(NotFoundException) as assert_error:
            self.use_case.execute(request)
        self.assertEqual(
            assert_error.exception.args[0], "Entity not found using ID 'not_found'"
        )

    def test_execute(self):
        category = Category(name="test")
        self.category_repo.items = [category]
        with patch.object(
            self.category_repo, "update", wraps=self.category_repo.update
        ) as spy_update:
            request = UpdateCategoryUseCase.Input(
                id=category.id,
                name="test 1",
            )
            response = self.use_case.execute(request)
            spy_update.assert_called_once()
            self.assertEqual(
                response,
                UpdateCategoryUseCase.Output(
                    id=category.id,
                    name="test 1",
                    description=None,
                    is_active=True,
                    created_at=category.created_at,
                ),
            )

        arrange = [
            {
                "input": {
                    "id": category.id,
                    "name": "test 2",
                    "description": "test description",
                },
                "expected": {
                    "id": category.id,
                    "name": "test 2",
                    "description": "test description",
                    "is_active": True,
                    "created_at": category.created_at,
                },
            },
            {
                "input": {
                    "id": category.id,
                    "name": "test",
                },
                "expected": {
                    "id": category.id,
                    "name": "test",
                    "description": None,
                    "is_active": True,
                    "created_at": category.created_at,
                },
            },
            {
                "input": {
                    "id": category.id,
                    "name": "test",
                    "is_active": False,
                },
                "expected": {
                    "id": category.id,
                    "name": "test",
                    "description": None,
                    "is_active": False,
                    "created_at": category.created_at,
                },
            },
            {
                "input": {"id": category.id, "name": "test", "is_active": True},
                "expected": {
                    "id": category.id,
                    "name": "test",
                    "description": None,
                    "is_active": True,
                    "created_at": category.created_at,
                },
            },
            {
                "input": {
                    "id": category.id,
                    "name": "test",
                    "description": "test description",
                    "is_active": False,
                },
                "expected": {
                    "id": category.id,
                    "name": "test",
                    "description": "test description",
                    "is_active": False,
                    "created_at": category.created_at,
                },
            },
        ]

        for i in arrange:
            request = UpdateCategoryUseCase.Input(**i["input"])
            response = self.use_case.execute(request)
            self.assertEqual(response, UpdateCategoryUseCase.Output(**i["expected"]))
