import unittest
from datetime import datetime
from category.domain.entities import Category

class TestCategory(unittest.TestCase):

    def test_constructor(self):
        created_at = datetime.now()
        category = Category(
            name='Movie',
            description='some description',
            is_active=False,
            created_at=created_at
        )

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, False)
        self.assertEqual(category.created_at, created_at)
        self.assertIsInstance(category.created_at, datetime)
