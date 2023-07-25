from typing import Any
from src.__shared.domain.serializer import CustomSerializer
from src.__shared.domain.validators.interface import ValidatorFieldsInterface
from src.category.domain.validators.category_validator import (
    DRFCategoryValidator,
    CustomCategoryValidator,
)


class CategoryValidatorFactory:
    @staticmethod
    def create(category_rule_class: Any) -> ValidatorFieldsInterface:
        if issubclass(category_rule_class, CustomSerializer):
            return CustomCategoryValidator(rule_class=category_rule_class)

        return DRFCategoryValidator(rule_class=category_rule_class)
