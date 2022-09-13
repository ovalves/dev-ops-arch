from dataclasses import dataclass


@dataclass()
class Event:
    code: str
    description: str
    price: int
