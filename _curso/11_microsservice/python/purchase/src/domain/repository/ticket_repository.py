from abc import ABC, abstractmethod
from typing import Any


class TicketRepository(ABC):
    @abstractmethod
    async def save(self, event: any) -> Any:
        pass

    @abstractmethod
    async def get(self, code: str) -> Any:
        pass

    @abstractmethod
    async def update(self, ticket: any) -> Any:
        pass
