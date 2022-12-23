from consumer import consumer

def main():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue

        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        print(msg.value().decode("utf-8"))

    # consumer.close()


if __name__ == "__main__":
    main()
