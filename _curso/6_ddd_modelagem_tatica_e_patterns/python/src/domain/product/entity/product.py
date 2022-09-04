from dataclasses import dataclass

@dataclass()
class Product:
    __id: str
    __name: str
    __price: int = 0

    def __post_init__(self):
        self.validate()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> int:
        return self.__price

    def change_name(self, name: str) -> None:
        self.__name = name
        self.validate()

    def change_price(self, price: int) -> None:
        self.__price = price
        self.validate()

    def validate(self) -> None:
        if len(self.__id) == 0:
            raise Exception("Id is required")

        if len(self.__name) == 0:
            raise Exception("Name is required")

        if self.__price <= 0:
            raise Exception("Price must be greater than zero")