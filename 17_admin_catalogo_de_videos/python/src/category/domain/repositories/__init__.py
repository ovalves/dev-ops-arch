from abc import ABC
from src.category.domain.entities.category import Category
from src.__shared.domain.repositories.interface import RepositoryInterface
from src.__shared.domain.repositories.search import SearchParams as DefaultSearchParams
from src.__shared.domain.repositories.search import SearchResult as DefaultSearchResult


class _SearchParams(DefaultSearchParams):
    pass


class _SearchResult(DefaultSearchResult):
    pass


class CategoryRepository(RepositoryInterface[Category], ABC):
    SearchParams = _SearchParams
    SearchResult = _SearchResult
