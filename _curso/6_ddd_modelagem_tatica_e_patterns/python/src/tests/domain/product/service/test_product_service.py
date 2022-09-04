from unittest import TestCase
from domain.product.entity.product import Product
from domain.product.service.product_service import ProductService

class TestProductService(TestCase):
    def test_should_change_the_prices_of_all_products(self):
        product1 = Product("product1", "Product 1", 10)
        product2 = Product("product2", "Product 2", 20)
        products = [product1, product2]

        ProductService.increase_price(products, 100)
        self.assertEqual(product1.price, 20)
        self.assertEqual(product2.price, 40)