from unittest import TestCase
from dataclasses import is_dataclass
from domain.product.entity.product import Product

class TestProduct(TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Product))

    def test_should_throw_error_when_id_is_empty(self):
        with self.assertRaises(Exception) as context:
            Product("", "Product 1")
        self.assertEqual("Id is required", str(context.exception))

    def test_should_throw_error_when_name_is_empty(self):
        with self.assertRaises(Exception) as context:
            Product("123", "")
        self.assertEqual("Name is required", str(context.exception))

    def test_should_throw_error_when_price_is_less_than_zero(self):
        with self.assertRaises(Exception) as context:
            Product("123", "Product 1", -1)
        self.assertEqual("Price must be greater than zero", str(context.exception))

    def test_should_change_name(self):
        # Arrange
        product = Product("123", "Product 1", 100)

        # Act
        product.change_name("Product 2")

        # Assert
        self.assertEqual(product.name, "Product 2")

    def test_should_change_price(self):
        # Arrange
        product = Product("123", "Product 1", 100)

        # Act
        product.change_price(150)

        # Assert
        self.assertEqual(product.price, 150)
