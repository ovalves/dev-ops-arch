from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic
from src.__shared.types import ErrorFields, PropsValidated


@dataclass(slots=True)
class ValidatorFieldsInterface(ABC, Generic[PropsValidated]):
    errors: ErrorFields = None
    validated_data: PropsValidated = None

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError()
