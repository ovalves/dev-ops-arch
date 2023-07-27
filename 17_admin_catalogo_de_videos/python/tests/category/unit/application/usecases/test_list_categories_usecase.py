from pprint import pprint
import unittest
from datetime import timedelta, timezone, datetime
from unittest.mock import patch

from src.core.category.domain.repositories import CategoryRepository
from src.core.__shared.domain.exceptions import NotFoundException
from src.core.__shared.application.usecases import UseCase
from src.core.__shared.application.dto.search_input import SearchInput
from src.core.__shared.application.dto.pagination_output import PaginationOutput
from src.core.__shared.application.mapper.pagination_output_mapper import (
    PaginationOutputMapper,
)
from src.core.category.application.dto.category_output import CategoryOutput
from src.core.category.application.mapper.category_output_mapper import (
    CategoryOutputMapper,
)
from src.core.category.domain.entities.category import Category
from src.core.category.infra.repositories.in_memory import CategoryInMemoryRepository
from src.core.category.application.usecases.list_categories_usecase import (
    ListCategoriesUseCase,
)


class TestListCategoriesUseCaseUnit(unittest.TestCase):
    use_case: ListCategoriesUseCase
    category_repo: CategoryInMemoryRepository

    def setUp(self) -> None:
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = ListCategoriesUseCase(self.category_repo)

    def test_instance_use_case(self):
        self.assertIsInstance(self.use_case, UseCase)

    def test_input(self):
        self.assertTrue(issubclass(ListCategoriesUseCase.Input, SearchInput))

    def test_output(self):
        self.assertTrue(issubclass(ListCategoriesUseCase.Output, PaginationOutput))

    def test__to_output(self):
        entity = Category(name="Movie")
        default_props = {
            "total": 1,
            "current_page": 1,
            "per_page": 2,
            "sort": None,
            "sort_dir": None,
            "filter": None,
        }

        result = CategoryRepository.SearchResult(items=[], **default_props)
        output = self.use_case._ListCategoriesUseCase__to_output(  # pylint: disable=protected-access
            result
        )
        self.assertEqual(
            output,
            ListCategoriesUseCase.Output(
                items=[],
                total=1,
                current_page=1,
                per_page=2,
                last_page=1,
            ),
        )

        result = CategoryRepository.SearchResult(items=[entity], **default_props)
        output = self.use_case._ListCategoriesUseCase__to_output(result)
        items = [CategoryOutputMapper.without_child().to_output(entity)]
        self.assertEqual(
            output,
            PaginationOutputMapper.from_child(ListCategoriesUseCase.Output).to_output(
                items, result
            ),
        )

    def test_execute_using_empty_search_params(self):
        self.category_repo.items = [
            Category(name="test 1"),
            Category(name="test 2", created_at=datetime.now()),
        ]
        with patch.object(
            self.category_repo, "search", wraps=self.category_repo.search
        ) as spy_search:
            input_param = ListCategoriesUseCase.Input()
            output = self.use_case.execute(input_param)
            spy_search.assert_called_once()
            self.assertEqual(
                output,
                ListCategoriesUseCase.Output(
                    items=list(
                        map(
                            CategoryOutputMapper.without_child().to_output,
                            self.category_repo.items[::-1],
                        )
                    ),
                    total=2,
                    current_page=1,
                    per_page=20,
                    last_page=1,
                ),
            )

    def test_execute_using_pagination_and_sort_and_filter(self):
        items = [
            Category(name="a"),
            Category(name="AAA"),
            Category(name="AaA"),
            Category(name="b"),
            Category(name="c"),
        ]
        self.category_repo.items = items

        input_param = ListCategoriesUseCase.Input(
            page=1, per_page=2, sort="name", sort_dir="asc", filter="a"
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(
            output,
            ListCategoriesUseCase.Output(
                items=list(
                    map(
                        CategoryOutputMapper.without_child().to_output,
                        [items[1], items[2]],
                    )
                ),
                total=3,
                current_page=1,
                per_page=2,
                last_page=2,
            ),
        )

        input_param = ListCategoriesUseCase.Input(
            page=2, per_page=2, sort="name", sort_dir="asc", filter="a"
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(
            output,
            ListCategoriesUseCase.Output(
                items=list(
                    map(CategoryOutputMapper.without_child().to_output, [items[0]])
                ),
                total=3,
                current_page=2,
                per_page=2,
                last_page=2,
            ),
        )

        input_param = ListCategoriesUseCase.Input(
            page=1, per_page=2, sort="name", sort_dir="desc", filter="a"
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(
            output,
            ListCategoriesUseCase.Output(
                items=list(
                    map(
                        CategoryOutputMapper.without_child().to_output,
                        [items[0], items[2]],
                    )
                ),
                total=3,
                current_page=1,
                per_page=2,
                last_page=2,
            ),
        )

        input_param = ListCategoriesUseCase.Input(
            page=2, per_page=2, sort="name", sort_dir="desc", filter="a"
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(
            output,
            ListCategoriesUseCase.Output(
                items=list(
                    map(CategoryOutputMapper.without_child().to_output, [items[1]])
                ),
                total=3,
                current_page=2,
                per_page=2,
                last_page=2,
            ),
        )
