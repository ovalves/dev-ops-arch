import unittest
from typing import List, Optional
from src.core.__shared.domain.entities import Entity
from src.core.__shared.domain.types import ENTITY, Filter
from src.core.__shared.domain.repositories.search import SearchResult
from src.core.__shared.domain.repositories.memory import InMemoryRepository
from src.core.__shared.domain.exceptions import NotFoundException
from src.core.__shared.domain.value_objects import UniqueEntityId
from tests.__shared.stubs import StubEntity


class TestSearchParamsResult(unittest.TestCase):
    def test_props_annotations(self):
        self.assertEqual(
            SearchResult.__annotations__,
            {
                "items": List[ENTITY],
                "total": int,
                "current_page": int,
                "per_page": int,
                "last_page": int,
                "sort": Optional[str],
                "sort_dir": Optional[str],
                "filter": Optional[Filter],
            },
        )

    def test_constructor(self):
        entity = StubEntity(name="fake", price=5)
        result = SearchResult(
            items=[entity, entity], total=4, current_page=1, per_page=2
        )

        self.assertDictEqual(
            result.to_dict(),
            {
                "items": [entity, entity],
                "total": 4,
                "current_page": 1,
                "per_page": 2,
                "last_page": 2,
                "sort": None,
                "sort_dir": None,
                "filter": None,
            },
        )

        result = SearchResult(
            items=[entity, entity],
            total=4,
            current_page=1,
            per_page=2,
            sort="name",
            sort_dir="asc",
            filter="test",
        )

        self.assertDictEqual(
            result.to_dict(),
            {
                "items": [entity, entity],
                "total": 4,
                "current_page": 1,
                "per_page": 2,
                "last_page": 2,
                "sort": "name",
                "sort_dir": "asc",
                "filter": "test",
            },
        )

    def test_when_per_page_is_greater_than_total(self):
        result = SearchResult(
            items=[],
            total=4,
            current_page=1,
            per_page=15,
        )
        self.assertEqual(result.last_page, 1)

    def test_when_per_page_is_less_than_total_and_they_are_not_multiples(self):
        result = SearchResult(
            items=[],
            total=101,
            current_page=1,
            per_page=20,
        )
        self.assertEqual(result.last_page, 6)
