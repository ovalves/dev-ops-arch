from unittest import IsolatedAsyncioTestCase
from domain.customer.entity.customer import Customer
from domain.customer.value_object.address import Address
from infrastructure.customer.repository.customer_memory_repository import CustomerMemoryRepository

class TestCustomerMemoryRepository(IsolatedAsyncioTestCase):
    async def test_should_create_a_customer(self):
        # Arrange
        customer_repository = CustomerMemoryRepository()
        customer = Customer("123", "Customer 1")
        address = Address("Street 1", 1, "Zipcode 1", "City 1")
        customer.set_address(address)
        await customer_repository.create(customer)

        # Act
        model_saved = await customer_repository.find(id=customer.id)
        model_saved_as_json = {
            "id": "123",
            "name": model_saved.name,
            "active": model_saved.is_active(),
            "rewardPoints": model_saved.reward_points,
            "street": model_saved.address.street,
            "number": model_saved.address.number,
            "zipcode": model_saved.address.zip,
            "city": model_saved.address.city,
        }

        # Assert
        self.assertEqual(
            model_saved_as_json,
            {
                "id": customer.id,
                "name": customer.name,
                "active": customer.is_active(),
                "rewardPoints": customer.reward_points,
                "street": customer.address.street,
                "number": customer.address.number,
                "zipcode": customer.address.zip,
                "city": customer.address.city,
            }
        )

    async def test_should_update_a_customer(self):
        # Arrange
        customer_repository = CustomerMemoryRepository()
        customer = Customer("123", "Customer 1")
        address = Address("Street 1", 1, "Zipcode 1", "City 1")
        customer.set_address(address)
        await customer_repository.create(customer)

        # Act
        customer.change_name("Name Updated")
        await customer_repository.update(customer)
        model_saved = await customer_repository.find(id=customer.id)
        model_saved_as_json = {
            "id": model_saved.id,
            "name": model_saved.name,
            "active": model_saved.is_active(),
            "rewardPoints": model_saved.reward_points,
            "street": model_saved.address.street,
            "number": model_saved.address.number,
            "zipcode": model_saved.address.zip,
            "city": model_saved.address.city,
        }

        # Assert
        self.assertEqual(
            model_saved_as_json,
            {
                "id": customer.id,
                "name": customer.name,
                "active": customer.is_active(),
                "rewardPoints": customer.reward_points,
                "street": customer.address.street,
                "number": customer.address.number,
                "zipcode": customer.address.zip,
                "city": customer.address.city,
            }
        )

    async def test_should_find_a_customer(self):
        # Arrange
        customer_repository = CustomerMemoryRepository()
        customer = Customer("123", "Customer 1")
        address = Address("Street 1", 1, "Zipcode 1", "City 1")
        customer.set_address(address)
        await customer_repository.create(customer)

        # Act
        model_found = await customer_repository.find(id=customer.id)
        model_found_as_json = {
            "id": model_found.id,
            "name": model_found.name,
            "active": model_found.is_active(),
            "rewardPoints": model_found.reward_points,
            "street": model_found.address.street,
            "number": model_found.address.number,
            "zipcode": model_found.address.zip,
            "city": model_found.address.city,
        }

        # Assert
        self.assertEqual(
            model_found_as_json,
            {
                "id": customer.id,
                "name": customer.name,
                "active": customer.is_active(),
                "rewardPoints": customer.reward_points,
                "street": customer.address.street,
                "number": customer.address.number,
                "zipcode": customer.address.zip,
                "city": customer.address.city,
            }
        )

    async def test_should_throw_an_error_when_customer_is_not_found(self):
        with self.assertRaises(Exception) as context:
            customer_repository = CustomerMemoryRepository()
            await customer_repository.find(id='1234')

        self.assertEqual("Customer not found", str(context.exception))

    async def test_should_find_all_customers(self):
        # Arrange
        customer_repository = CustomerMemoryRepository()

        # Creating Customer 1
        customer1 = Customer("123", "Customer 1")
        address1 = Address("Street 1", 1, "Zipcode 1", "City 1")
        customer1.set_address(address1)

        # Creating Customer 2
        customer2 = Customer("456", "Customer 2")
        address2 = Address("Street 2", 2, "Zipcode 2", "City 2")
        customer2.set_address(address2)

        # Act
        await customer_repository.create(customer1)
        await customer_repository.create(customer2)
        customers = await customer_repository.find_all()

        # Assert
        self.assertEqual(len(customers), 2)