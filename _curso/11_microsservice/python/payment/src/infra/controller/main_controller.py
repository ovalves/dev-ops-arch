from dataclasses import dataclass
from application.process_transaction import ProcessTransaction
from domain.dtos.process_transaction_dto import ProcessTransactionDTO
from infra.http.http_server import HttpServer
from infra.http.schema.base_error import BaseError
from fastapi import Response, status


@dataclass()
class MainController:
    http_server: HttpServer
    process_transaction: ProcessTransaction

    def __post_init__(self):
        @self.http_server.post(
            "/v1/transactions",
            status_code=200,
            responses={400: {"model": BaseError}, 500: {"model": BaseError}},
        )
        def transaction(data: ProcessTransactionDTO, response: Response):
            try:
                return self.process_transaction.execute(data)
            except Exception as ex:
                print(ex)
                response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                response.content = "Process Transaction Failed"
                return {
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "detail": {"Process Transaction Failed"},
                }
