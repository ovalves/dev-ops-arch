from dataclasses import dataclass

@dataclass()
class Address:
    __street: str = ''
    __number: int = 0
    __zip: str = ''
    __city: str = ''

    def __post_init__(self):
        self.validate()

    @property
    def street(self) -> str:
        return self.__street

    @property
    def number(self) -> int:
        return self.__number

    @property
    def zip(self) -> str:
        return self.__zip

    @property
    def city(self) -> str:
        return self.__city

    def validate(self) -> None:
        if len(self.__street) == 0:
            raise Exception("Street is required")

        if self.__number == 0:
            raise Exception("Number is required")

        if len(self.__zip) == 0:
            raise Exception("Street is required")

        if len(self.__city) == 0:
            raise Exception("Street is required")

    def __str__(self) -> str:
        return f"{self.__street}, {self.__number}, {self.__zip} {self.__city}"