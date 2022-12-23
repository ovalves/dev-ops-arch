from consumer import get_message, close_consumer

def main():
    while True:
        msg = get_message()
        if msg is None:
            continue

        if msg.error():
            print(f"Error: {msg.error()}")
            continue


        print("===================")
        print(msg.value().decode("utf-8"))
        print("===================")

    # close_consumer()


if __name__ == "__main__":
    main()
