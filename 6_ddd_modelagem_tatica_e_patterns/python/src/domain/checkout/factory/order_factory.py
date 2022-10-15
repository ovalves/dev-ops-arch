from typing import Dict
from domain.checkout.entity.order import Order
from domain.checkout.entity.order_item import OrderItem

# props = {
#     'id': 'string',
#     'customer_id': 'string',
#     'items': [
#         {
#             'id': '123',
#             'name': 'item 1',
#             'productId': 'product 1',
#             'quantity': 1,
#             'price': 15,
#         }
#     ]
# }
class OrderFactory:
    @staticmethod
    def create(props: Dict) -> Order:
        items = list(
                    map(
                        lambda item: OrderItem(
                            item['id'],
                            item['name'],
                            item['price'],
                            item['productId'],
                            item['quantity'],
                        ),
                        props['items']
                    )
                )

        return Order(props['id'], props['customer_id'], items)