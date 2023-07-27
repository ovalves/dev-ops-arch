import unittest
from typing import Optional
from datetime import datetime
from src.core.category.application.dto.category_output import CategoryOutput


class TestCategoryOutputDtoUnit(unittest.TestCase):
    def test_fields(self):
        self.assertEqual(
            CategoryOutput.__annotations__,
            {
                "id": str,
                "name": str,
                "description": Optional[str],
                "is_active": bool,
                "created_at": datetime,
            },
        )
