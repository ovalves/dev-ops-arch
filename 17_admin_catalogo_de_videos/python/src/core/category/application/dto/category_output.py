from typing import Optional
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CategoryOutput:
    id: str
    name: str
    description: Optional[str]
    is_active: bool
    created_at: datetime
