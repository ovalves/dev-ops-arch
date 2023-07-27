import unittest
from typing import Optional
from unittest.mock import patch
from src.core.__shared.application.usecases import UseCase
from src.core.category.application.dto.category_output import CategoryOutput
from src.core.category.domain.entities.category import Category
from src.core.category.infra.repositories.in_memory import CategoryInMemoryRepository
from src.core.category.application.usecases.create_category_usecase import (
    CreateCategoryUseCase,
)


class TestCreateCategoryUseCaseUnit(unittest.TestCase):
    use_case: CreateCategoryUseCase
    category_repo: CategoryInMemoryRepository

    def setUp(self) -> None:
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = CreateCategoryUseCase(self.category_repo)

    def test_if_instance_a_use_case(self):
        self.assertIsInstance(self.use_case, UseCase)

    def test_input(self):
        self.assertEqual(
            CreateCategoryUseCase.Input.__annotations__,
            {
                "name": str,
                "description": Optional[str],
                "is_active": Optional[bool],
            },
        )

        description_field = CreateCategoryUseCase.Input.__dataclass_fields__[
            "description"
        ]
        self.assertEqual(
            description_field.default, Category.get_field("description").default
        )

        is_active_field = CreateCategoryUseCase.Input.__dataclass_fields__["is_active"]
        self.assertEqual(
            is_active_field.default, Category.get_field("is_active").default
        )

    def test_output(self):
        self.assertTrue(issubclass(CreateCategoryUseCase.Output, CategoryOutput))

    def test_execute(self):
        with patch.object(
            self.category_repo, "insert", wraps=self.category_repo.insert
        ) as spy_insert:
            input_param = CreateCategoryUseCase.Input(name="Movie")
            output = self.use_case.execute(input_param)
            spy_insert.assert_called_once()
            self.assertEqual(
                output,
                CreateCategoryUseCase.Output(
                    id=self.category_repo.items[0].id,
                    name="Movie",
                    description=None,
                    is_active=True,
                    created_at=self.category_repo.items[0].created_at,
                ),
            )

        input_param = CreateCategoryUseCase.Input(
            name="Movie", description="some description", is_active=False
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(
            output,
            CreateCategoryUseCase.Output(
                id=self.category_repo.items[1].id,
                name="Movie",
                description="some description",
                is_active=False,
                created_at=self.category_repo.items[1].created_at,
            ),
        )

        input_param = CreateCategoryUseCase.Input(
            name="Movie", description="some description", is_active=True
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(
            output,
            CreateCategoryUseCase.Output(
                id=self.category_repo.items[2].id,
                name="Movie",
                description="some description",
                is_active=True,
                created_at=self.category_repo.items[2].created_at,
            ),
        )
