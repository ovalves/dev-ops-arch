import Customer from './domain/customer/entity/customer';
import Address from './domain/customer/value_objects/address';
import OrderItem from './domain/entity/aggregate/order_item';
import Order from './domain/entity/aggregate/order';

// Customer Aggregate
let customer = new Customer("123", "Vinicius");
const address = new Address("Rua cinco", 131, "12345-678", "São Paulo");
customer.Address = address;

// Order Aggregate
const item1 = new OrderItem("1", "Item 1", 10, "product1", 1);
const item2 = new OrderItem("2", "Item 2", 15, "product2", 1);
const item3 = new OrderItem("3", "Item 3", 25, "product3", 1);
const order = new Order("1", "123", [item1, item2, item3]);