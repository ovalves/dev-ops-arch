from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from category.factory.category_validator_factory import CategoryValidatorFactory
from __shared.domain.entities import Entity
from src.__shared.domain.exceptions import EntityValidationException
from src.__shared.domain.validators.custom_validator_adapter import CustomValidatorAdapter


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

    # @classmethod
    # def validate(cls, name: str, description: str, is_active: bool = None):
    #     CustomValidatorAdapter.values(name, "name").required().string().max_length(255)
    #     CustomValidatorAdapter.values(description, "description").string()
    #     CustomValidatorAdapter.values(is_active, "is_active").boolean()

    def validate(self):
        validator = CategoryValidatorFactory.create()
        is_valid = validator.validate(self.to_dict())
        if not is_valid:
            raise EntityValidationException(validator.errors)
