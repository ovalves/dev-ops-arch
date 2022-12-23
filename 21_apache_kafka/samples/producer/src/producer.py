import json
import time
import random
from faker import Faker
from confluent_kafka import Producer
from logger import log

fake = Faker()

producer = Producer({"bootstrap.servers": "localhost:9094"})
print("Kafka Producer has been initiated...")

def message_sender_callback(error, message):
    if error is not None:
        log.error(error)
        print(f"Error: {error}")
        return

    message = f'Produced message on topic: {message.topic()} | value: {message.value().decode("utf-8")}\n'
    log.info(message)
    print(message)

def send_message(data):
    message = json.dumps(data)
    producer.poll(1)
    producer.produce("students", message.encode("utf-8"), callback=message_sender_callback)
    producer.flush()