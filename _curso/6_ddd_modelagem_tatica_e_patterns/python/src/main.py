from domain.customer.entity.customer import Customer
from domain.customer.value_object.address import Address
from domain.entity.aggregate.order_item import OrderItem
from domain.entity.aggregate.order import Order
from domain.checkout.factory.order_factory import OrderFactory

props = {
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
            'price': 37,
        }
    ]
}

OrderFactory().create(props)

# # Customer Aggregate
# customer = Customer(
#     "123",
#     "Customer"
# )
# address = Address("Rua cinco", 131, "12345-678", "São Paulo")
# customer.set_address(address)

# # // Order Aggregate
# item1 = OrderItem("1", "Item 1", 10, "product1", 1)
# item2 = OrderItem("2", "Item 2", 15, "product2", 1)
# item3 = OrderItem("3", "Item 3", 25, "product3", 1)
# order = Order("1", "123", [item1, item2, item3])

# print(order.total)