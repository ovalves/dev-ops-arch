from typing import Dict, List, Any, TypeVar
from src.__shared.domain.entities import Entity

ErrorFields = Dict[str, List[str]]
PropsValidated = TypeVar("PropsValidated")
ENTITY = TypeVar("ENTITY", bound=Entity)
Input = TypeVar("Input")
Output = TypeVar("Output")
Filter = TypeVar("Filter", str, Any)
