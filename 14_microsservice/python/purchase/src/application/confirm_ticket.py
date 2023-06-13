from dataclasses import dataclass
from infra.repository.ticket_memory_repository import TicketMemoryRepository


@dataclass()
class ConfirmTicket:
    ticket_repository: TicketMemoryRepository

    def execute(self, code: str) -> None:
        ticket = self.ticket_repository.get(code)
        ticket.status = "confirmed"

        self.ticket_repository.update(ticket)
        print(ticket)
