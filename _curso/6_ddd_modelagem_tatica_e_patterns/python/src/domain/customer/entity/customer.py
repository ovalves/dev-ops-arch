from dataclasses import dataclass, field
from typing import Optional
from domain.customer.value_object.address import Address

@dataclass()
class Customer:
    __id: str
    __name: str
    __address: Optional[Address] = None
    __active: Optional[bool] = True
    __rewardPoints: Optional[int] = 0

    def __post_init__(self):
        self.validate()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def reward_points(self) -> int:
        return self.__rewardPoints

    @property
    def  address(self) -> Address:
        return self.__address

    def set_address(self, address: Address) -> None:
        self.__address = address

    def changeName(self, name: str) -> None:
        self.__name = name
        self.validate()

    def changeAddress(self, address: Address) -> None:
        self.__address = address
        self.validate()

    def activate(self) -> None:
        if not isinstance(self.__address, Address):
            raise Exception("Address is mandatory to activate a customer")

        self.__active = True

    def deactivate(self) -> None:
        self.__active = False

    def is_active(self) -> bool:
        return self.__active

    def validate(self) -> None:
        if len(self.__id) == 0:
            raise Exception("Id is required")

        if len(self.__name) == 0:
            raise Exception("Name is required")

    def addRewardPoints(self, points: int) -> None:
        self.__rewardPoints += points