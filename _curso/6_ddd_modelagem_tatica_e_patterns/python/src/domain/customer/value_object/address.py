from dataclasses import dataclass

@dataclass()
class Address:
    _street: str = ''
    _number: int = 0
    _zip: str = ''
    _city: str = ''

    def __post_init__(self):
        self.validate()

    @property
    def street(self) -> str:
        return self._street

    @property
    def number(self) -> int:
        return self._number

    @property
    def zip(self) -> str:
        return self._zip

    @property
    def city(self) -> str:
        return self._city

    def validate(self) -> None:
        if len(self._street) == 0:
            raise Exception("Street is required")

        if self._number == 0:
            raise Exception("Number is required")

        if len(self._zip) == 0:
            raise Exception("Street is required")

        if len(self._city) == 0:
            raise Exception("Street is required")

    def __str__(self) -> str:
        return f"{self._street}, {self._number}, {self._zip} {self._city}"