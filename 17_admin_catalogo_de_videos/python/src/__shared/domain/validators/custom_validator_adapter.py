from abc import ABC
from src.__shared.domain.types import PropsValidated
from src.__shared.domain.validators.interface import ValidatorFieldsInterface


class CustomValidatorAdapter(ValidatorFieldsInterface[PropsValidated], ABC):
    """Adaptador de validação de regras da entidade Categoria
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
