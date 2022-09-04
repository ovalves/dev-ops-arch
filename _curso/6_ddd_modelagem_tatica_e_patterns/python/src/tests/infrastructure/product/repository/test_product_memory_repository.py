from itertools import product
from unittest import IsolatedAsyncioTestCase
from domain.product.entity.product import Product
from infrastructure.product.repository.product_memory_repository import ProductMemoryRepository

class TestProductMemoryRepository(IsolatedAsyncioTestCase):
    async def test_should_create_a_product(self):
        # Arrange
        product_repository = ProductMemoryRepository()
        product = Product("1", "Product 1", 100)
        await product_repository.create(product)

        # Act
        model_saved = await product_repository.find(id=product.id)
        model_saved_as_json = {
            "id": model_saved.id,
            "name": model_saved.name,
            "price": model_saved.price,
        }

        # Assert
        self.assertEqual(
            model_saved_as_json,
            {
                "id": "1",
                "name": "Product 1",
                "price": 100,
            }
        )

    async def test_should_update_a_product(self):
        # Arrange
        product_repository = ProductMemoryRepository()
        product = Product("1", "Product 1", 100)
        await product_repository.create(product)

        # Act
        model_saved = await product_repository.find(id=product.id)
        model_saved_as_json = {
            "id": model_saved.id,
            "name": model_saved.name,
            "price": model_saved.price,
        }

        # Assert
        self.assertEqual(
            model_saved_as_json,
            {
                "id": "1",
                "name": "Product 1",
                "price": 100,
            }
        )

        # Arrange
        # Change product data
        product.change_name("Product 2")
        product.change_price(200)
        # Update Product data
        await product_repository.update(product)
        # Get Updated Product
        model_updated = await product_repository.find(id=product.id)
        model_updated_as_json = {
            "id": model_updated.id,
            "name": model_updated.name,
            "price": model_updated.price,
        }

        # Assert
        self.assertEqual(
            model_updated_as_json,
            {
                "id": "1",
                "name": "Product 2",
                "price": 200,
            }
        )

    async def test_should_find_a_product(self):
        # Arrange
        product_repository = ProductMemoryRepository()
        product = Product("1", "Product 1", 100)
        await product_repository.create(product)

        model_found = await product_repository.find(id=product.id)
        model_found_as_json = {
            "id": model_found.id,
            "name": model_found.name,
            "price": model_found.price,
        }

        # Assert
        self.assertEqual(
            model_found_as_json,
            {
                "id": "1",
                "name": "Product 1",
                "price": 100,
            }
        )

    async def test_should_find_all_products(self):
        # Arrange
        product_repository = ProductMemoryRepository()

        # Creating Product 1
        product1 = Product("1", "Product 1", 100)

        # Creating Product 2
        product2 = Product("2", "Product 2", 200)

        # Act
        await product_repository.create(product1)
        await product_repository.create(product2)

        products = await product_repository.find_all()

        # Assert
        self.assertEqual(len(products), 2)