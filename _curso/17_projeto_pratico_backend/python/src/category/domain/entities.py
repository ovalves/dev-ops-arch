from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from __shared.domain.entities import Entity

@dataclass(kw_only=True, frozen=True)
class Category(Entity):
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
    )
