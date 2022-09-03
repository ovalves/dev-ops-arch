from unittest import TestCase
from unittest.mock import patch
from domain.__shared.event.event_dispatcher import EventDispatcher
from domain.product.event.handler.send_email_when_product_is_created_handler import SendEmailWhenProductIsCreatedHandler
from domain.product.event.product_created_event import ProductCreatedEvent

class TestEventDispatcher(TestCase):
    def test_should_register_an_event_handler(self):
        # Arrange
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        # Act
        event_dispatcher.register('ProductCreatedEvent', event_handler)
        handlers = event_dispatcher.get_event_handlers()

        # Assert
        self.assertIsNotNone(handlers['ProductCreatedEvent'])
        self.assertEqual(len(handlers['ProductCreatedEvent']), 1)
        self.assertEqual(handlers['ProductCreatedEvent'][0], event_handler)

    def test_should_unregister_an_event_handler(self):
        # Arrange
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        # Act
        event_dispatcher.register('ProductCreatedEvent', event_handler)
        handlers = event_dispatcher.get_event_handlers()

        # Assert
        self.assertEqual(handlers['ProductCreatedEvent'][0], event_handler)

        # Act
        event_dispatcher.unregister('ProductCreatedEvent', event_handler)

        # Assert
        self.assertIsNotNone(handlers['ProductCreatedEvent'])
        self.assertEqual(len(handlers['ProductCreatedEvent']), 0)

    def test_should_unregister_all_event_handlers(self):
        # Arrange
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        # Act
        event_dispatcher.register('ProductCreatedEvent', event_handler)

        # Assert
        self.assertEqual(event_dispatcher.get_event_handlers()['ProductCreatedEvent'][0], event_handler)

        #Act
        event_dispatcher.unregister_all()

        # Assert
        self.assertEqual(len(event_dispatcher.get_event_handlers()), 0)

    def test_should_notify_all_event_handlers(self):
        # Arrange
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        # Act
        event_dispatcher.register('ProductCreatedEvent', event_handler)

        # Assert
        self.assertEqual(event_dispatcher.get_event_handlers()['ProductCreatedEvent'][0], event_handler)

        # Spy Object Method -> <SendEmailWhenProductIsCreatedHandler, handle>
        with patch.object(
            event_handler,
            'handle',
            autospec=True,
            side_effect=event_handler.handle
        ) as mock_event_handler:
            product_created_event = ProductCreatedEvent({
                'name': 'Product 1',
                'description': 'Product 1 description',
                'price': 10.0
            })
            event_dispatcher.notify(product_created_event);
            mock_event_handler.assert_called_once()

