from typing import Dict, List, TypeVar
from __shared.domain.entities import Entity

ErrorFields = Dict[str, List[str]]
PropsValidated = TypeVar("PropsValidated")
ENTITY = TypeVar("ENTITY", bound=Entity)
