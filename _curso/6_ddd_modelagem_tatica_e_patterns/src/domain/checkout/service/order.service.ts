import { v4 as uuid } from "uuid";
import Order from "../../../entity/aggregate/order";
import OrderItem from "../../../entity/aggregate/order_item";
import Customer from "../../../entity/customer";

export default class OrderService {
    static placeOrder(customer: Customer, items: OrderItem[]): Order {
        if (items.length === 0) {
            throw new Error("Order must have at least one item");
        }
        const order = new Order(uuid(), customer.id, items);
        customer.addRewardPoints(order.total() / 2);
        return order;
    }

    static total(orders: Order[]): number {
        return orders.reduce((acc, order) => acc + order.total(), 0);
    }
}