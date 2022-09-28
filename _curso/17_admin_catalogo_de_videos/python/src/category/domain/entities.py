from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from __shared.domain.entities import Entity
from __shared.domain.exceptions import EntityValidationException
from __shared.domain.validators import ValidatorRules
from category.domain.validators import CategoryValidatorFactory


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
    #     ValidatorRules.values(name, "name").required().string().max_length(255)
    #     ValidatorRules.values(description, "description").string()
    #     ValidatorRules.values(is_active, "is_active").boolean()

    def validate(self):
        validator = CategoryValidatorFactory.create()
        is_valid = validator.validate(self.to_dict())
        if not is_valid:
            raise EntityValidationException(validator.errors)
