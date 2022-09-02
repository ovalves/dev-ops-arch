from dataclasses import dataclass
from typing import List
from functools import reduce

from domain.entity.aggregate.order_item import OrderItem

@dataclass()
class Order:
    __id: str
    __customer_id: str
    __items: List[OrderItem]
    __total: int = 0

    def __post_init__(self):
        self.__total = self.calculate_total()
        self.validate()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def customer_id(self) -> str:
        return self.__customer_id

    @property
    def items(self) -> List[OrderItem]:
        return self.__items

    @property
    def total(self) -> int:
        return self.__total

    def calculate_total(self) -> int:
        return reduce(lambda total, item: total + item.price, self.__items, 0)
        return sum([item.price for item in self.__items])

    def validate(self) -> bool:
        if len(self.__id) == 0:
            raise Exception("Id is required")

        if len(self.customer_id) == 0:
            raise Exception("CustomerId is required")

        if len(self.__items) == 0:
            raise Exception("Items are required")

        if any(list(map(lambda item: item.quantity <= 0, self.__items))):
            raise Exception("Quantity must be greater than 0")

        return True