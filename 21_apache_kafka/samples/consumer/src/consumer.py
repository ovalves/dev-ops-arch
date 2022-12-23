from confluent_kafka import Consumer

consumer = Consumer(
    {
        "bootstrap.servers": "localhost:9094",
        "group.id": "python-consumer",
        "auto.offset.reset": "earliest",
    }
)

print("Kafka Consumer has been initiated...")
consumer.subscribe(["students"])

def get_message():
    return consumer.poll(1.0)

def close_consumer():
    return consumer.close()