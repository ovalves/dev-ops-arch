# pylint: disable=unexpected-keyword-arg

import unittest
import time
from datetime import datetime
from category.domain.entities import Category
from dataclasses import is_dataclass, FrozenInstanceError

class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

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

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category(name='Movie 1')
        time.sleep(0.1)
        category2 = Category(name='Movie 2')

        self.assertNotEqual(
            category1.created_at.timestamp(),
            category2.created_at.timestamp()
        )

    def test_UniqueEntityId_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Category(name='Movie 1')
            value_object.name = 'Movie 3'

    def test_update(self):
        category = Category(name='Movie')
        category.update('Documentary', 'some description')
        self.assertEqual(category.name, 'Documentary')
        self.assertEqual(category.description, 'some description')

    def test_activate(self):
        category = Category(name='Movie', is_active=False)
        category.activate()
        self.assertTrue(category.is_active)

    def test_deactivate(self):
        category = Category(name='Movie')
        category.deactivate()
        self.assertFalse(category.is_active)
