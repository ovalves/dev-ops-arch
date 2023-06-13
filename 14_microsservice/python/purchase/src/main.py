from uuid import uuid4
from domain.entity.event import Event
from application.purchase_ticket import PurchaseTicket
from application.get_ticket import GetTicket
from application.confirm_ticket import ConfirmTicket
from infra.repository.event_memory_repository import EventMemoryRepository
from infra.repository.ticket_memory_repository import TicketMemoryRepository
from infra.gateway.payment_gateway import PaymentGateway
from infra.http.fast_api_adapter import FastApiAdapter
from infra.http.aiohttp_adapter import AioHttpAdapter
from infra.queue.rabbitmq_adapter import RabbitMQAdapter
from infra.controller.main_controller import MainController
from infra.consumer.ticket_consumer import TicketConsumer


def init():
    # Client | Server
    http_server = FastApiAdapter()
    http_client = AioHttpAdapter()

    # Repositories
    ticket_repository = TicketMemoryRepository()
    event_repository = EventMemoryRepository()
    event_repository.save(Event("2RTC7", "Microservice Python", 100))

    # Payment Gateway
    payment_gateway = PaymentGateway(http_client)

    # RabbitMQ
    queue = RabbitMQAdapter()
    queue.connect()

    # Test Purchase
    purchase_ticket = PurchaseTicket(
        ticket_repository, event_repository, payment_gateway, queue
    )
    get_ticket = GetTicket(ticket_repository, event_repository)

    # Purchase API - Controller
    MainController(http_server, purchase_ticket, get_ticket, queue)

    # Ticket Confirmation
    confirm_ticket = ConfirmTicket(ticket_repository)

    # Ticket Consumer
    ticket_consumer = TicketConsumer(queue, confirm_ticket, purchase_ticket)
    ticket_consumer.consume()

    # Server Listen
    http_server.listen(5000)


if __name__ == "__main__":
    init()
