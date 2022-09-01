import uuid
import json
from abc import ABC
from dataclasses import dataclass, field, fields
from __shared.domain.exceptions import InvalidUuidException

@dataclass(frozen=True, slots=True)
class ValueObject(ABC):
    def __str__(self) -> str:
        fields_name = [field.name for field in fields(self)]
        return str(getattr(self, fields_name[0])) \
            if len(fields_name) == 1 \
            else json.dumps({field_name: getattr(self, field_name) for field_name in fields_name})

@dataclass(frozen=True)
class UniqueEntityId(ValueObject):
    __id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __post_init__(self):
        id_value = str(self.__id) if isinstance(self.__id, uuid.UUID) else self.__id
        object.__setattr__(self, '__id', id_value)
        self.__validate()

    @property
    def id(self):
        return self.__id

    def __validate(self):
        try:
            uuid.UUID(self.__id)
        except ValueError as ex:
            raise InvalidUuidException() from ex
