from abc import ABC, abstractmethod
from typing import Any, Generic
from dataclasses import dataclass
from src.__shared.domain.types import ErrorFields, ClsPropsValidated, PropsValidated


@dataclass(slots=True)
class ValidatorFieldsInterface(ABC, Generic[PropsValidated]):
    errors: ErrorFields = None
    validated_data: PropsValidated = None
    rule_class: ClsPropsValidated = None

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError()
