from dataclasses import dataclass
from infra.repository.event_memory_repository import EventMemoryRepository
from infra.repository.ticket_memory_repository import TicketMemoryRepository

@dataclass(kw_only=True)
class Output:
    participant_email: str
    event_description: str
    status: str
    total: int

@dataclass()
class GetTicket:
    ticket_repository: TicketMemoryRepository
    event_repository: EventMemoryRepository

    def execute(self, code: str) -> Output:
        ticket = self.ticket_repository.get(code)
        event = self.event_repository.get(ticket.event_code)

        return Output(
            participant_email=ticket.participant_email,
            event_description=event.description,
            status=ticket.status,
            total=ticket.total,
        )