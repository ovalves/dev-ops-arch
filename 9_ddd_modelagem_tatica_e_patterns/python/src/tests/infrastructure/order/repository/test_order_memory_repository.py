from unittest import IsolatedAsyncioTestCase
from domain.customer.entity.customer import Customer
from domain.customer.value_object.address import Address
from domain.product.entity.product import Product
from domain.checkout.entity.order import Order
from domain.checkout.entity.order_item import OrderItem
from infrastructure.order.repository.order_memory_repository import OrderMemoryRepository
from infrastructure.customer.repository.customer_memory_repository import CustomerMemoryRepository
from infrastructure.product.repository.product_memory_repository import ProductMemoryRepository

class TestOrderMemoryRepository(IsolatedAsyncioTestCase):
    async def test_should_create_a_new_order(self):
        # Arrange

        # Creating a customer
        customer_repository = CustomerMemoryRepository()
        customer = Customer("customer:459EAT", "Customer 1")
        address = Address("Street 1", 1, "Zipcode 1", "City 1")
        customer.set_address(address)
        await customer_repository.create(customer)

        # Creating a product
        product_repository = ProductMemoryRepository()
        product = Product("product:785PAT", "Product 1", 10)
        await product_repository.create(product)

        # Creating an order item
        ordem_item = OrderItem("item:1", product.name, product.price, product.id, 2)

        # Creating an order
        order = Order("order:121TIP", customer.id, [ordem_item])

        # Saving the order
        order_repository = OrderMemoryRepository()
        await order_repository.create(order)
        model_saved = await order_repository.find(id=order.id)
        model_saved_as_json = {
            "id": model_saved.id,
            "customer_id": model_saved.customer_id,
            "total": model_saved.total,
            "items": [
                {
                    "id": model_saved.items[0].id,
                    "name": model_saved.items[0].name,
                    "price": model_saved.items[0].price,
                    "quantity": model_saved.items[0].quantity,
                    "order_id": model_saved.id,
                    "product_id": model_saved.items[0].product_id,
                },
            ],
        }
        self.assertEqual(
            model_saved_as_json,
            {
                "id": "order:121TIP",
                "customer_id": "customer:459EAT",
                "total": 20,
                "items": [
                    {
                        "id": "item:1",
                        "name": "Product 1",
                        "price": 20,
                        "quantity": 2,
                        "order_id": "order:121TIP",
                        "product_id": "product:785PAT",
                    },
                ],
            }
        )
