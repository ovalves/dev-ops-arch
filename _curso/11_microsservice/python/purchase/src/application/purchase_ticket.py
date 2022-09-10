from typing import Any
from dataclasses import dataclass
from domain.entity.ticket import Ticket
from infra.repository.event_memory_repository import EventMemoryRepository
from infra.repository.ticket_memory_repository import TicketMemoryRepository
from infra.gateway.payment_gateway import PaymentGateway
from infra.queue.queue_interface import QueueInterface

@dataclass()
class Input:
    ticket_code: str
    participant_name: str
    participant_email: str
    event_code: str
    credit_card_number: str
    credit_card_cvv: str
    credit_card_exp_date: str


@dataclass()
class PurchaseTicket:
    ticket_repository: TicketMemoryRepository
    event_repository: EventMemoryRepository
    payment_gateway: PaymentGateway
    queue: QueueInterface

    def execute(self, input: Input) -> Any:
        event = self.event_repository.get(input.event_code)
        ticket = Ticket(
            input.ticket_code,
            input.participant_name,
            input.participant_email,
            input.credit_card_number,
            input.credit_card_cvv,
            input.credit_card_exp_date,
            event
        )

        self.ticket_repository.save(ticket)

        self.queue.publish("ticketPurchased", {
			"external_code": input.ticket_code,
			"credit_card_number": input.credit_card_number,
			"credit_card_cvv": input.credit_card_cvv,
			"credit_card_exp_date": input.credit_card_exp_date,
			"total": ticket.total
		})