from unittest import TestCase
from domain.product.factory.product_factory import ProductFactory

class TestProductService(TestCase):
    def test_should_create_a_product(self):
        product = ProductFactory.create('Product A', 100)
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, 'Product A')
        self.assertEqual(product.price, 100)
