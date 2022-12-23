import json
import time
import random
from faker import Faker
from producer import send_message
fake = Faker()

def main():
    for _ in range(10):
        data = {
            "id": fake.random_int(min=20000, max=100000),
            "name": fake.name(),
            "street": fake.street_address(),
            "city": fake.city(),
            "code": fake.country_code(),
            "platform": random.choice(["Mobile", "Laptop", "Tablet"]),
            "signup_at": str(fake.date_time_this_month()),
        }

        send_message(data)
        time.sleep(3)


if __name__ == "__main__":
    main()
