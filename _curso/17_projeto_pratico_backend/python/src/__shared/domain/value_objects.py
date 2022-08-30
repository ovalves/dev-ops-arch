import uuid
from dataclasses import dataclass, field
from __shared.domain.exceptions import InvalidUuidException


@dataclass()
class UniqueEntityId:
    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __post_init__(self):
        self.id = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        self.__validate()

    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as ex:
            raise InvalidUuidException() from ex
