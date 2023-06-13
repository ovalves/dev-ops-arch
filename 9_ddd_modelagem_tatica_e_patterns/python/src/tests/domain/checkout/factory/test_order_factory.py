from unittest import TestCase
from domain.checkout.factory.order_factory import OrderFactory


class TestOrderFactory(TestCase):
    def test_should_create_an_order(self):
        order_props = {
            'id': 'order 1',
            'customer_id': '123',
            'items': [
                {
                    'id': '123',
                    'name': 'order 1',
                    'productId': 'item 1',
                    'quantity': 1,
                    'price': 15,
                },
                {
                    'id': '456',
                    'name': 'order 2',
                    'productId': 'item 2',
                    'quantity': 1,
                    'price': 35,
                },
                {
                    'id': '789',
                    'name': 'order 3',
                    'productId': 'item 3',
                    'quantity': 1,
                    'price': 50,
                }
            ]
        }

        order = OrderFactory().create(order_props)
        self.assertEqual(order.id, order_props['id'])
        self.assertEqual(order.customer_id, order_props['customer_id'])
        self.assertEqual(len(order.items), 3)
        self.assertEqual(order.total, 100)