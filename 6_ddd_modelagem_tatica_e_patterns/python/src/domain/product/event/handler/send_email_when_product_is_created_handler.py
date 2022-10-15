from domain.__shared.event.event_handler_interface import EventHandlerInterface
from domain.product.event.product_created_event import ProductCreatedEvent

class SendEmailWhenProductIsCreatedHandler(EventHandlerInterface):
    def handle(self, event: ProductCreatedEvent) -> None:
        print(vars(event))
        print('Sending email to...')