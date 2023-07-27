from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field
from src.core.category.domain.factory.category_validator_factory import (
    CategoryValidatorFactory,
)
from src.core.__shared.domain.entities import Entity
from src.core.__shared.domain.exceptions import EntityValidationException
from src.core.__shared.domain.validators.custom_validator_adapter import (
    CustomValidatorAdapter,
)
from src.core.__shared.domain.serializer import CustomSerializer
from rest_framework import serializers
from src.core.__shared.domain.validators.drf_validator_adapter import (
    DRFStrictBooleanField,
    DRFStrictCharField,
)


class DRFCategoryRules(serializers.Serializer):
    name = DRFStrictCharField(max_length=255)
    description = DRFStrictCharField(required=False, allow_null=True, allow_blank=True)
    is_active = DRFStrictBooleanField(required=False)
    created_at = serializers.DateTimeField(required=False)


class CustomCategoryRules(CustomSerializer):
    name = "string|required|max_length:255"
    description = "max_length:255"
    is_active = "boolean"
    created_at = ""


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(Entity):
    name: str = ""
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.created_at:
            self._set("created_at", datetime.now())

        self.validate()

    def update(self, name: str, description: str) -> None:
        self._set("name", name)
        self._set("description", description)
        self.validate()

    def activate(self) -> None:
        self._set("is_active", True)

    def deactivate(self) -> None:
        self._set("is_active", False)

    def validate(self):
        validator = CategoryValidatorFactory.create(DRFCategoryRules)
        is_valid = validator.validate(self.to_dict())
        if not is_valid:
            raise EntityValidationException(validator.errors)
