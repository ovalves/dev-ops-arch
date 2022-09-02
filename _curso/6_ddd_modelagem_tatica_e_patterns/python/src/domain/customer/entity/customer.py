from dataclasses import dataclass, field
from typing import Optional
from domain.customer.value_object.address import Address

@dataclass()
class Customer:
    _id: str
    _name: str
    _address: Optional[Address] = None
    _active: Optional[bool] = True
    _rewardPoints: Optional[int] = 0

    def __post_init__(self):
        self.validate()

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def reward_points(self) -> int:
        return self._rewardPoints

    @property
    def  address(self) -> Address:
        return self._address

    def set_address(self, address: Address) -> None:
        self._address = address

    def changeName(self, name: str) -> None:
        self._name = name
        self.validate()

    def changeAddress(self, address: Address) -> None:
        self._address = address
        self.validate()

    def activate(self) -> None:
        if not isinstance(self._address, Address):
            raise Exception("Address is mandatory to activate a customer")

        self._active = True

    def deactivate(self) -> None:
        self._active = False

    def is_active(self) -> bool:
        return self._active

    def validate(self) -> None:
        if len(self._id) == 0:
            raise Exception("Id is required")

        if len(self._name) == 0:
            raise Exception("Name is required")

    def addRewardPoints(self, points: int) -> None:
        self._rewardPoints += points