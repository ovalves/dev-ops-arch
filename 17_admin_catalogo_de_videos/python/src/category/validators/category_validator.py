from typing import Dict
from src.category.rules.drf_category_rules import DRFCategoryRules
from src.category.rules.custom_category_rules import CustomCategoryRules
from src.__shared.domain.validators.drf_validator_adapter import DRFValidatorAdapter
from src.__shared.domain.validators.custom_validator_adapter import CustomValidatorAdapter


class DRFCategoryValidator(
    DRFValidatorAdapter
):  # pylint: disable=too-few-public-methods
    def validate(self, data: Dict) -> bool:
        rules = DRFCategoryRules(data=data if data is not None else {})
        return super().validate(rules)


class CustomCategoryValidator(
    CustomValidatorAdapter
):  # pylint: disable=too-few-public-methods
    def validate(self, data: Dict) -> bool:
        rules = CustomCategoryRules(data=data if data is not None else {})
        return super().validate(rules)
