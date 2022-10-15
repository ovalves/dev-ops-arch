from unittest import TestCase
from dataclasses import is_dataclass
from domain.entity.aggregate.order import Order
from domain.entity.aggregate.order_item import OrderItem


class TestOrder(TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Order))

    def test_should_throw_error_when_id_is_empty(self):
        with self.assertRaises(Exception) as context:
            Order("", "123", [])
        self.assertEqual("Id is required", str(context.exception))

    def test_should_throw_error_when_customerId_is_empty(self):
        with self.assertRaises(Exception) as context:
            Order("123", "", [])
        self.assertEqual("CustomerId is required", str(context.exception))

    def test_should_throw_error_when_Items_is_empty(self):
        with self.assertRaises(Exception) as context:
            Order("123", "123", [])
        self.assertEqual("Items are required", str(context.exception))

    def test_should_calculate_total(self):
        # Arrange
        item1 = OrderItem("item1", "Item 1", 100, "product1", 1)
        item2 = OrderItem("item2", "Item 2", 200, "product2", 2)
        item3 = OrderItem("item2", "Item 2", 300, "product2", 3)

        order = Order("order1", "customer1", [item1, item2])
        total = order.calculate_total()
        # Assert
        self.assertEqual(total, 500)

        # Arrange
        order = Order("order2", "customer2", [item1, item2, item3])
        total = order.calculate_total()
        # Assert
        self.assertEqual(total, 1400)

    def test_should_throw_error_if_item_qte_is_less_or_equal_zero(self):
        with self.assertRaises(Exception) as context:
            item = OrderItem("item1", "Item 1", 100, "product1", -1)
            Order("order1", "customer1", [item]);
        self.assertEqual("Quantity must be greater than 0", str(context.exception))