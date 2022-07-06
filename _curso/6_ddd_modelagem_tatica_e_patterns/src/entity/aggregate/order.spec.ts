import Order from "./order";
import OrderItem from "./order_item";

describe("Order unit tests", () => {
    it("should throw error when id is empty", () => {
        expect(() => {
            let order = new Order("", "123", []);
        }).toThrowError("Id is required");
    });

    it("should throw error when customerId is empty", () => {
        expect(() => {
            let order = new Order("123", "", []);
        }).toThrowError("CustomerId is required");
    });

    it("should throw error when customerId is empty", () => {
        expect(() => {
            let order = new Order("123", "123", []);
        }).toThrowError("Items are required");
    });

    it("should calculate total", () => {
        const item = new OrderItem("item1", "Item 1", 100, "product1", 1);
        const item2 = new OrderItem("item2", "Item 2", 200, "product2", 2);
        const item3 = new OrderItem("item2", "Item 2", 300, "product2", 3);
        const order = new Order("order1", "customer1", [item, item2]);

        let total = order.total();

        expect(order.total()).toBe(500);

        const order2 = new Order("order1", "customer1", [item, item2, item3]);
        total = order2.total();
        expect(total).toBe(1400);
    });

    it("should throw error if the item qte is less or equal zero 0", () => {
        expect(() => {
            const item = new OrderItem("i1", "Item 1", 100, "p1", 0);
            const order = new Order("o1", "c1", [item]);
        }).toThrowError("Quantity must be greater than 0");
    });
});
