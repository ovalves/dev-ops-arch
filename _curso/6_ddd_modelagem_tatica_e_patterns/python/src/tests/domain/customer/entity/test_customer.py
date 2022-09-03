from unittest import TestCase
from dataclasses import is_dataclass
from domain.customer.entity.customer import Customer
from domain.customer.value_object.address import Address


class TestCustomer(TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Customer))

    def test_should_throw_error_when_id_is_empty(self):
        with self.assertRaises(Exception) as context:
            Customer("", "John")
        self.assertEqual("Id is required", str(context.exception))

    def test_should_throw_error_when_name_is_empty(self):
        with self.assertRaises(Exception) as context:
            Customer("123", "")
        self.assertEqual("Name is required", str(context.exception))

    def test_should_change_name(self):
        # Arrange
        customer = Customer("123", "John")

        # Act
        customer.change_name("Jane")

        # Assert
        self.assertEqual("Jane", customer.name)

    def test_should_activate_customer(self):
        customer = Customer("1", "Customer 1")
        address = Address("Rua cinco", 131, "12345-678", "São Paulo")
        customer.set_address(address)
        customer.activate()

        self.assertTrue(customer.is_active())

    def test_should_throw_error_if_address_is_none_on_activate_a_customer(self):
        with self.assertRaises(Exception) as context:
            customer = Customer("1", "Customer 1")
            customer.activate()

        self.assertEqual("Address is mandatory to activate a customer", str(context.exception))

    def test_should_deactivate_customer(self):
        # Arrange
        customer = Customer("123", "John")

        # Act
        customer.deactivate()

        # Assert
        self.assertFalse(customer.is_active())

    def test_should_add_reward_points(self):
        customer = Customer("123", "John")
        self.assertEqual(customer.reward_points, 0)

        customer.add_reward_points(10)
        self.assertEqual(customer.reward_points, 10)

        customer.add_reward_points(10)
        self.assertEqual(customer.reward_points, 20)