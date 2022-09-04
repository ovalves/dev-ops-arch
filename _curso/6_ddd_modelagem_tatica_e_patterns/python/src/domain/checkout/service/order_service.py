import uuid
from functools import reduce
from typing import List
from domain.checkout.entity.order import Order
from domain.checkout.entity.order_item import OrderItem
from domain.customer.entity.customer import Customer

class OrderService:
    @staticmethod
    def place_order(customer: Customer, items: List[OrderItem]) -> Order:
        if not items:
            raise Exception("Order must have at least one item")

        order = Order(str(uuid.uuid4()), customer.id, items)
        customer.add_reward_points(order.total / 2)
        return order

    @staticmethod
    def total(orders: List[Order]) -> int:
        return reduce(lambda total, order: total + order.total, orders, 0)