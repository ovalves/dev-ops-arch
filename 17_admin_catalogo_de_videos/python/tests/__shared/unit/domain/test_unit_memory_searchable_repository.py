import unittest
from tests.__shared.stubs import (
    StubEntity,
    StubInMemorySearchableRepository,
)
from src.__shared.domain.repositories.search import SearchResult, SearchParams


class TestInMemorySearchableRepository(unittest.TestCase):

    repo: StubInMemorySearchableRepository

    def setUp(self) -> None:
        self.repo = StubInMemorySearchableRepository()

    def test__apply_filter(self):
        items = [StubEntity(name="test", price=5)]
        result = self.repo._apply_filter(items, None)
        self.assertEqual(items, result)

        items = [
            StubEntity(name="test", price=5),
            StubEntity(name="TEST", price=5),
            StubEntity(name="fake", price=0),
        ]

        # pylint: disable=protected-access
        result = self.repo._apply_filter(items, "TEST")
        self.assertEqual([items[0], items[1]], result)

        # pylint: disable=protected-access
        result = self.repo._apply_filter(items, "5")
        self.assertEqual([items[0], items[1]], result)

    def test__apply_sort(self):
        items = [
            StubEntity(name="b", price=1),
            StubEntity(name="a", price=0),
            StubEntity(name="c", price=2),
        ]

        arrange = [
            {"items": items, "name": "price", "direction": "asc", "expected": items},
            {
                "items": items,
                "name": "name",
                "direction": "asc",
                "expected": [items[1], items[0], items[2]],
            },
            {
                "items": items,
                "name": "name",
                "direction": "desc",
                "expected": [items[2], items[0], items[1]],
            },
            {
                "items": items,
                "name": "price",
                "direction": "desc",
                "expected": [items[0], items[1], items[2]],
            },
        ]

        for i in arrange:
            result = self.repo._apply_sort(i["items"], i["name"], i["direction"])
            self.assertEqual(i["expected"], result)

    def test__apply_paginate(self):
        items = [
            StubEntity(name="a", price=1),
            StubEntity(name="b", price=1),
            StubEntity(name="c", price=1),
            StubEntity(name="d", price=1),
            StubEntity(name="e", price=1),
        ]

        result = self.repo._apply_paginate(items, 1, 2)
        self.assertEqual([items[0], items[1]], result)

        result = self.repo._apply_paginate(items, 2, 2)
        self.assertEqual([items[2], items[3]], result)

        result = self.repo._apply_paginate(items, 3, 2)
        self.assertEqual([items[4]], result)

        result = self.repo._apply_paginate(items, 4, 2)
        self.assertEqual([], result)

    def test_search_when_params_is_empty(self):
        entity = StubEntity(name="a", price=1)
        items = [entity] * 15
        self.repo.items = items

        result = self.repo.search(SearchParams())
        self.assertEqual(
            result,
            SearchResult(
                items=[entity] * 15,
                total=15,
                current_page=1,
                per_page=20,
                sort=None,
                sort_dir=None,
                filter=None,
            ),
        )

    def test_search_applying_filter_and_paginate(self):
        items = [
            StubEntity(name="test", price=1),
            StubEntity(name="a", price=1),
            StubEntity(name="TEST", price=1),
            StubEntity(name="TeSt", price=1),
        ]
        self.repo.items = items

        result = self.repo.search(SearchParams(page=1, per_page=2, filter="TEST"))
        self.assertEqual(
            result,
            SearchResult(
                items=[items[0], items[2]],
                total=3,
                current_page=1,
                per_page=2,
                sort=None,
                sort_dir=None,
                filter="TEST",
            ),
        )

        result = self.repo.search(SearchParams(page=2, per_page=2, filter="TEST"))
        self.assertEqual(
            result,
            SearchResult(
                items=[items[3]],
                total=3,
                current_page=2,
                per_page=2,
                sort=None,
                sort_dir=None,
                filter="TEST",
            ),
        )

        result = self.repo.search(SearchParams(page=3, per_page=2, filter="TEST"))
        self.assertEqual(
            result,
            SearchResult(
                items=[],
                total=3,
                current_page=3,
                per_page=2,
                sort=None,
                sort_dir=None,
                filter="TEST",
            ),
        )

    def test_search_applying_sort_and_paginate(self):
        items = [
            StubEntity(name="b", price=1),
            StubEntity(name="a", price=1),
            StubEntity(name="d", price=1),
            StubEntity(name="e", price=1),
            StubEntity(name="c", price=1),
        ]
        self.repo.items = items

        arrange_by_asc = [
            {
                "input": SearchParams(page=1, per_page=2, sort="name"),
                "output": SearchResult(
                    items=[items[1], items[0]],
                    total=5,
                    current_page=1,
                    per_page=2,
                    sort="name",
                    sort_dir="asc",
                    filter=None,
                ),
            },
            {
                "input": SearchParams(page=2, per_page=2, sort="name"),
                "output": SearchResult(
                    items=[items[4], items[2]],
                    total=5,
                    current_page=2,
                    per_page=2,
                    sort="name",
                    sort_dir="asc",
                    filter=None,
                ),
            },
            {
                "input": SearchParams(page=3, per_page=2, sort="name"),
                "output": SearchResult(
                    items=[items[3]],
                    total=5,
                    current_page=3,
                    per_page=2,
                    sort="name",
                    sort_dir="asc",
                    filter=None,
                ),
            },
        ]

        for index, item in enumerate(arrange_by_asc):
            result = self.repo.search(item["input"])
            self.assertEqual(
                result,
                item["output"],
                f"The output using sort_dir asc on index {index} is different",
            )

        arrange_by_desc = [
            {
                "input": SearchParams(page=1, per_page=2, sort="name", sort_dir="desc"),
                "output": SearchResult(
                    items=[items[3], items[2]],
                    total=5,
                    current_page=1,
                    per_page=2,
                    sort="name",
                    sort_dir="desc",
                    filter=None,
                ),
            },
            {
                "input": SearchParams(page=2, per_page=2, sort="name", sort_dir="desc"),
                "output": SearchResult(
                    items=[items[4], items[0]],
                    total=5,
                    current_page=2,
                    per_page=2,
                    sort="name",
                    sort_dir="desc",
                    filter=None,
                ),
            },
            {
                "input": SearchParams(page=3, per_page=2, sort="name", sort_dir="desc"),
                "output": SearchResult(
                    items=[items[1]],
                    total=5,
                    current_page=3,
                    per_page=2,
                    sort="name",
                    sort_dir="desc",
                    filter=None,
                ),
            },
        ]

        for index, item in enumerate(arrange_by_desc):
            result = self.repo.search(item["input"])
            self.assertEqual(
                result,
                item["output"],
                f"The output using sort_dir desc on index {index} is different",
            )

    def test_search_applying_filter_and_sort_and_paginate(self):
        items = [
            StubEntity(name="test", price=1),
            StubEntity(name="a", price=1),
            StubEntity(name="TEST", price=1),
            StubEntity(name="e", price=1),
            StubEntity(name="TeSt", price=1),
        ]
        self.repo.items = items

        result = self.repo.search(
            SearchParams(page=1, per_page=2, sort="name", sort_dir="asc", filter="TEST")
        )

        self.assertEqual(
            result,
            SearchResult(
                items=[items[2], items[4]],
                total=3,
                current_page=1,
                per_page=2,
                sort="name",
                sort_dir="asc",
                filter="TEST",
            ),
        )

        result = self.repo.search(
            SearchParams(page=2, per_page=2, sort="name", sort_dir="asc", filter="TEST")
        )

        self.assertEqual(
            result,
            SearchResult(
                items=[items[0]],
                total=3,
                current_page=2,
                per_page=2,
                sort="name",
                sort_dir="asc",
                filter="TEST",
            ),
        )
