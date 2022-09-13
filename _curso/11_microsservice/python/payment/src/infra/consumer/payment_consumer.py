from dataclasses import dataclass
from application.process_transaction import ProcessTransaction
from infra.queue.queue_interface import QueueInterface


@dataclass()
class PaymentConsumer:
    queue: QueueInterface
    process_transaction: ProcessTransaction

    def consume(self):
        self.queue.consume("ticketPurchased", self.process_transaction.execute)
