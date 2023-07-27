from abc import ABC
from typing import Any, Dict
from dataclasses import Field, dataclass, field, asdict
from src.core.__shared.domain.value_objects import UniqueEntityId


@dataclass(frozen=True)
class Entity(ABC):
    unique_entity_id: UniqueEntityId = field(default_factory=lambda: UniqueEntityId())

    @property
    def id(self) -> str:
        return str(self.unique_entity_id)

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self) -> Dict:
        entity_dict = asdict(self)
        entity_dict.pop("unique_entity_id")
        entity_dict["id"] = self.id
        return entity_dict

    @classmethod
    def get_field(cls, entity_field: str) -> Field:
        return cls.__dataclass_fields__[entity_field]
