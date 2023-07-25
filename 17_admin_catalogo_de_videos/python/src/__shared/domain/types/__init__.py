from typing import Dict, List, Any, TypeVar
from src.__shared.domain.entities import Entity
from src.__shared.application.dtos.pagination_output import (
    PaginationOutput as PaginationOutputBound,
)
from src.category.application.dtos.category_output import (
    CategoryOutput as CategoryOutputBound,
)

ErrorFields = Dict[str, List[str]]
ClsPropsValidated = TypeVar("ClsPropsValidated")
PropsValidated = TypeVar("PropsValidated")
ENTITY = TypeVar("ENTITY", bound=Entity)
Item = TypeVar("Item")
Input = TypeVar("Input")
Output = TypeVar("Output")
Filter = TypeVar("Filter", str, Any)
PaginationOutput = TypeVar("PaginationOutput", bound=PaginationOutputBound)
CategoryOutputType = TypeVar("CategoryOutputType", bound=CategoryOutputBound)
