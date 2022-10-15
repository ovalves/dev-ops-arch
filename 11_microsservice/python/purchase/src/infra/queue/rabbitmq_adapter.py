import json
import pika
from typing import Any, Callable
from infra.queue.queue_interface import QueueInterface


class RabbitMQAdapter(QueueInterface):
    connection: None

    def connect(self) -> Any:
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )

    def close(self) -> Any:
        self.connection.close()

    def consume(self, event_name: str, callback: Callable) -> Any:
        def on_message(channel, method_frame, header_frame, body):
            print(method_frame.delivery_tag)
            print(header_frame)
            print(body)
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)

        channel = self.connection.channel()
        channel.queue_declare(queue=event_name, durable=True)
        channel.basic_consume(event_name, on_message)

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            self.close()

    def publish(self, event_name: str, data: Any) -> Any:
        channel = self.connection.channel()
        channel.queue_declare(queue=event_name, durable=True)
        channel.confirm_delivery()

        try:
            channel.basic_publish(
                exchange=event_name,
                routing_key=event_name,
                body=json.dumps(data),
                properties=pika.BasicProperties(
                    content_type="text/plain", delivery_mode=pika.DeliveryMode.Transient
                ),
            )

            print("Message publish was confirmed")
        except pika.exceptions.UnroutableError:
            print("Message could not be confirmed")
