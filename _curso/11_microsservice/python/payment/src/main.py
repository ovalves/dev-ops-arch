from application.process_transaction import ProcessTransaction
from infra.http.fast_api_adapter import FastApiAdapter
from infra.queue.rabbitmq_adapter import RabbitMQAdapter
from infra.controller.main_controller import MainController
from infra.consumer.payment_consumer import PaymentConsumer

def init():
    # RabbitMQ
    queue = RabbitMQAdapter()
    queue.connect()

    # Client | Server
    http_server = FastApiAdapter()

    # Transaction Process
    process_transaction = ProcessTransaction(queue)

    # Purchase API - Controller
    MainController(http_server, process_transaction)

    # Payment Consumer
    payment_consumer = PaymentConsumer(queue, process_transaction)
    payment_consumer.consume()

    # Server Listen
    http_server.listen(5001)

if __name__ == '__main__':
    init()