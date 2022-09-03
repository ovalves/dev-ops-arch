from abc import ABC, abstractmethod
from typing import Any

class RepositoryInterface(ABC):
    @abstractmethod
    async def create(self, entity: any) -> Any:
        pass

    @abstractmethod
    async def update(self, entity: any) -> Any:
        pass

    @abstractmethod
    async def find(self, entity: any) -> Any:
        pass

    @abstractmethod
    async def findAll(self, entity: any) -> Any:
        pass