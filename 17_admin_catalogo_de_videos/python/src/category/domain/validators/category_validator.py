from typing import Dict
from src.__shared.domain.validators.drf_validator_adapter import DRFValidatorAdapter
from src.__shared.domain.validators.custom_validator_adapter import (
    CustomValidatorAdapter,
)


class DRFCategoryValidator(DRFValidatorAdapter):
    def validate(self, data: Dict) -> bool:
        return super().validate(self.rule_class(data=data if data is not None else {}))


class CustomCategoryValidator(CustomValidatorAdapter):
    def validate(self, data: Dict) -> bool:
        return super().validate(self.rule_class(data=data if data is not None else {}))
