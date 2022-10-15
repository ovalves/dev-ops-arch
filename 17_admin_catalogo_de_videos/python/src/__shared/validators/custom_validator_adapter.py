from abc import ABC
from dataclasses import dataclass
from typing import Any
from src.__shared.exceptions import ValidationException
from src.__shared.types import PropsValidated
from src.__shared.validators.interface import ValidatorFieldsInterface

# @dataclass(frozen=True)
# class CustomValidatorAdapter:
class CustomValidatorAdapter(
    ValidatorFieldsInterface[PropsValidated], ABC
):  # pylint: disable=too-few-public-methods
    """Adaptador de validação do Django Rest Framework
    Usage:
        ---

    Returns:
        True: Quando os campos são válidos
        False: Quando os campos NÃO são válidos
    """

    def validate(self, data) -> bool:
        serializer = data
        if serializer.is_valid:
            return True

        self.errors = serializer.errors
        return False
