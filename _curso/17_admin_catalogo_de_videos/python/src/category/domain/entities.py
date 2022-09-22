from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from __shared.domain.entities import Entity


@dataclass(frozen=True)
class Category(Entity):
    name: str = ""
    description: Optional[str] = None
    is_active: Optional[bool] = True

    # pylint: disable=unnecessary-lambda
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())

    def update(self, name: str, description: str) -> None:
        self._set("name", name)
        self._set("description", description)

    def activate(self) -> None:
        self._set("is_active", True)

    def deactivate(self) -> None:
        self._set("is_active", False)
