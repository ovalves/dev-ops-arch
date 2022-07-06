import Customer from './entity/customer';
import Address from './entity/value_objects/address';
import OrderItem from './entity/aggregate/order_item';
import Order from './entity/aggregate/order';

// Customer Aggregate
let customer = new Customer("123", "Vinicius");
const address = new Address("Rua cinco", 131, "12345-678", "São Paulo");
customer.Address = address;

// Order Aggregate
const item1 = new OrderItem("1", "Item 1", 10);
const item2 = new OrderItem("2", "Item 2", 15);
const item3 = new OrderItem("3", "Item 3", 25);
const order = new Order("1", "123", [item1, item2, item3]);
