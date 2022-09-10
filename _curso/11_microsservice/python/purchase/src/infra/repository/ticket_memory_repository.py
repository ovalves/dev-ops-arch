from typing import Any
from copy import deepcopy
from domain.repository.ticket_repository import TicketRepository
from domain.entity.ticket import Ticket

class TicketMemoryRepository(TicketRepository):
    __memory = {}

    def __init__(self):
        self.__memory = {}

    async def save(self, ticket: Ticket) -> Any:
        if ticket.event_code not in self.__memory:
            self.__memory[ticket.event_code] = []

        self.__memory[ticket.event_code].append(deepcopy(ticket))

    async def get(self, code: str) -> Any:
        if code not in self.__memory:
            raise Exception('Ticket not found')

        return self.__memory[code][0]

    async def update(self, entity: Ticket) -> Any:
        try:
            self.__memory.pop(entity.id, None)
            await self.create(entity)
        except Exception:
            raise Exception('Could not update ticket')