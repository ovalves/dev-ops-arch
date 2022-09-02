from dataclasses import dataclass

@dataclass()
class OrderItem:
    __id: str
    __name: str
    __price: int
    __product_id: str
    __quantity: int

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def price(self) -> int:
        return self.__price * self.__quantity