from dataclasses import dataclass
from application.get_ticket import GetTicket
from application.purchase_ticket import PurchaseTicket
from infra.http.http_server import HttpServer
from infra.queue.queue_interface import QueueInterface
import infra.routes.get_ticket_route as get_ticket_route
import infra.routes.purchase_route as purchase_route

def test():
    print('testing')

@dataclass()
class MainController:
    http_server: HttpServer
    purchase_ticker: PurchaseTicket
    get_ticket: GetTicket
    queue: QueueInterface

    def __post_init__(self):
        self.http_server.on("get_ticket", "get", "/tickets/:code", test)
        # self.http_server.app.include_router(
        #     purchase_route.router,
        #     tags=["Purchase Ticket"],
        #     prefix="/v1",
        # )
        # self.http_server.app.include_router(
        #     get_ticket_route.router,
        #     tags=["Get Tickets"],
        #     prefix="/v1",
        # )

