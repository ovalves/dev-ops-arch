from unittest import TestCase
from domain.checkout.entity.order import Order
from domain.checkout.entity.order_item import OrderItem
from domain.customer.entity.customer import Customer
from domain.checkout.service.order_service import OrderService

class TestOrderService(TestCase):
    def test_should_place_an_order(self):
        customer = Customer("c1", "Customer 1")
        item1 = OrderItem("i1", "Item 1", 10, "p1", 1)

        order = OrderService.place_order(customer, [item1])
        self.assertEqual(customer.reward_points, 5)
        self.assertEqual(order.total, 10)

    def test_should_get_total_of_all_orders(self):
        item1 = OrderItem("i1", "Item 1", 100, "p1", 1)
        item2 = OrderItem("i2", "Item 2", 200, "p2", 2)

        order = Order("o1", "c1", [item1])
        order2 = Order("o2", "c1", [item2])

        total = OrderService.total([order, order2])
        self.assertEqual(total, 500)