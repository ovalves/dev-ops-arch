from uuid import uuid4
from domain.entity.event import Event
from application.purchase_ticket import PurchaseTicket, Input as PurchaseTicketInput
from infra.repository.event_memory_repository import EventMemoryRepository
from infra.repository.ticket_memory_repository import TicketMemoryRepository
from infra.gateway.payment_gateway import PaymentGateway
from infra.http.fast_api_adapter import FastApiAdapter
from infra.http.aiohttp_adapter import AioHttpAdapter
from infra.queue.rabbitmq_adapter import RabbitMQAdapter
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
    purchase_ticket = PurchaseTicket(ticket_repository, event_repository, payment_gateway, queue)
    ticket_code = uuid4()
    purchase_ticket.execute(
        PurchaseTicketInput(
            ticket_code=ticket_code,
            participant_name="José",
            participant_email="josé@example.com",
            event_code="2RTC7",
            credit_card_number="0000.0000.0000.0000",
            credit_card_cvv="000",
            credit_card_exp_date="12/27"
        )
    )

    http_server.listen(5000)

if __name__ == '__main__':
    init()