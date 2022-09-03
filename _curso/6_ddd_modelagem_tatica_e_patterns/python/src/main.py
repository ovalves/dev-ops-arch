# from domain.customer.entity.customer import Customer
# from domain.customer.value_object.address import Address
# from domain.entity.aggregate.order_item import OrderItem
# from domain.entity.aggregate.order import Order

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

from domain.customer.repository.customer_repository_interface import CustomerRepositoryInterface
from domain.__shared.repository.repository_interface import RepositoryInterface

class EmlParserNew(CustomerRepositoryInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

print(dir(EmlParserNew()))