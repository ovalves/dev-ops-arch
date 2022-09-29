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
    """Validador customizado de campos de uma classe

    Raises:
        ValidationException: Quando o campo é obrigatório
        ValidationException: Quando o campo precisa ser string
        ValidationException: Quando ultrapassar o limite de caracteres
        ValidationException: Quando o campo precisa ser boolean

    Usage:
        CustomValidatorAdapter.values(name, "name").required().string().max_length(255)
        CustomValidatorAdapter.values(description, "description").string()

    Returns:
        CustomValidatorAdapter: Quando não houve erros na validação dos campos
        ValidationException: Quando houve erros na validação dos campos
    """

    def validate(self, data) -> bool:
        serializer = data
        if serializer.is_valid:
            return True

        self.errors = serializer.errors
        return False
