from dataclasses import dataclass
from application.get_ticket import GetTicket
from application.purchase_ticket import PurchaseTicket
from domain.dtos.purchase_ticket_dto import PurchaseTicketDTO
from infra.http.http_server import HttpServer
from infra.queue.queue_interface import QueueInterface
from infra.http.schema.base_error import BaseError
from fastapi import Response, status

@dataclass()
class MainController:
    http_server: HttpServer
    purchase_ticket: PurchaseTicket
    get_ticket: GetTicket
    queue: QueueInterface

    def __post_init__(self):
        @self.http_server.get("/v1/tickets/:code", status_code=200, responses={400: {'model': BaseError}, 500: {'model': BaseError}})
        async def read_item(code: str, response: Response):
            try:
                response.status_code = status.HTTP_200_OK
                return self.get_ticket.execute(code)
            except Exception as ex:
                print(ex)
                response.status_code = status.HTTP_404_NOT_FOUND
                response.content = 'Ticket Not Found'
                return {
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "detail": {
                        'Ticket Not Found'
                    }
                }

        @self.http_server.post("/v1/purchases", status_code=200, responses={400: {'model': BaseError}, 500: {'model': BaseError}})
        def purchase(data: PurchaseTicketDTO, response: Response):
            try:
                self.purchase_ticket.execute(data)
                self.queue.publish("purchaseTicket", data.json())
                return {}
            except Exception as ex:
                print(ex)
                response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                response.content = 'Purchase Ticket Failed'
                return {
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "detail": {
                        'Purchase Ticket Failed'
                    }
                }