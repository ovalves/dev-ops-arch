from dataclasses import dataclass
from application.confirm_ticket import ConfirmTicket
from application.purchase_ticket import PurchaseTicket
from infra.queue.queue_interface import QueueInterface
from infra.repository.ticket_memory_repository import TicketMemoryRepository

@dataclass()
class TicketConsumer:
    queue: QueueInterface
    confirm_ticket: ConfirmTicket
    purchase_ticket: PurchaseTicket

    def __post_init__(self):
        self.queue.consume("transactionApproved", self.confirm_ticket.execute)
        self.queue.consume("purchaseTicket", self.purchase_ticket.execute)
