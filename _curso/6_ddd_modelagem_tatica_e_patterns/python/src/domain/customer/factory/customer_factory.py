import uuid
from dataclasses import dataclass, field, fields
from domain.customer.entity.customer import Customer
from domain.customer.value_object.address import Address

class CustomerFactory:

    @staticmethod
    def create(name: str) -> Customer:
        return Customer(CustomerFactory.get_uuid(), name)

    @staticmethod
    def create_with_address(name: str, address: Address) -> Customer:
        customer = Customer(CustomerFactory.get_uuid(), name)
        customer.change_address(address)
        return customer

    @staticmethod
    def get_uuid() -> str:
        return str(uuid.uuid4())