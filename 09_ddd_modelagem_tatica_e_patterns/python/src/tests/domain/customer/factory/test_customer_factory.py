from unittest import TestCase
from domain.customer.factory.customer_factory import CustomerFactory
from domain.customer.value_object.address import Address

class TestCustomerFactory(TestCase):
    def test_should_create_a_customer(self):
        customer = CustomerFactory.create('John')
        self.assertEqual(customer.name, 'John')
        self.assertIsNotNone(customer.id)
        self.assertIsNone(customer.address)

    def test_should_create_a_customer_with_an_address(self):
        address = Address('Street', 1, '13330-250', 'São Paulo')
        customer = CustomerFactory.create_with_address(
            'John',
            address
        )

        self.assertEqual(customer.name, 'John')
        self.assertIsNotNone(customer.id)
        self.assertIsNotNone(customer.address)
        self.assertEqual(customer.address, address)


