from abc import ABC
from rest_framework.fields import BooleanField, CharField
from rest_framework.serializers import Serializer
from src.core.__shared.domain.types import PropsValidated
from src.core.__shared.domain.validators.interface import ValidatorFieldsInterface


class DRFValidatorAdapter(ValidatorFieldsInterface[PropsValidated], ABC):
    """Adaptador de validação do Django Rest Framework
    Usage:
        ---

    Returns:
        True: Quando os campos são válidos
        False: Quando os campos NÃO são válidos
    """

    def validate(self, data: Serializer) -> bool:
        serializer = data
        if serializer.is_valid():
            self.validated_data = dict(serializer.validated_data)
            return True

        self.errors = {
            field: [str(_error) for _error in _errors]
            for field, _errors in serializer.errors.items()
        }
        return False


class DRFStrictCharField(CharField):
    def to_internal_value(self, data):
        if not isinstance(data, str):
            self.fail("invalid")

        return super().to_internal_value(data)


class DRFStrictBooleanField(BooleanField):
    def to_internal_value(self, data):
        if data is True:
            return True
        if data is False:
            return False
        if data is None and self.allow_null:
            return None
        self.fail("invalid", input=data)
