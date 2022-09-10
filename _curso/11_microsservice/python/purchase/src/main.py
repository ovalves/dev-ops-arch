from uuid import uuid4
from domain.entity.event import Event
from application.purchase_ticket import PurchaseTicket
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
    event_repository.save(Event("C", "Imersão Full Cycle", 100))

    # Payment Gateway
    payment_gateway = PaymentGateway(http_client)

    # RabbitMQ
    queue = RabbitMQAdapter()
    queue.connect()

    # Test Purchase
    purchase_ticket = PurchaseTicket(ticket_repository, event_repository, payment_gateway, queue)
    ticket_code = uuid4()
    input = {
        "ticket_code": ticket_code,
		"participant_name": "A",
		"participant_email": "B",
		"event_code": "C",
		"credit_card_umber": "D",
		"credit_card_cvv": "E",
		"credit_card_exp_date": "F"
    }

    http_server.listen(5000)

if __name__ == '__main__':
    init()