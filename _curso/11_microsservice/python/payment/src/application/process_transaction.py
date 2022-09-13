from dataclasses import dataclass
from domain.dtos.process_transaction_dto import ProcessTransactionDTO
from infra.queue.queue_interface import QueueInterface


@dataclass()
class ProcessTransaction:
    queue: QueueInterface

    def execute(self, input: ProcessTransactionDTO) -> None:
        print(input)
        self.queue.publish(
            "transactionApproved",
            {"externalCode": input.external_code, "success": True},
        )
