import OrderItem from "./order_item";

export default class Order {
    _id: string;
    _customerID: string;
    _items: OrderItem[];
    _total: number;

    constructor(id: string, customerID: string, items: OrderItem[]) {
        this._id = id;
        this._customerID = customerID;
        this._items = items;
        this._total = this.total();
    }

    total(): number {
        return this._items.reduce((acc, item) => acc + item.price, 0);
    }
}