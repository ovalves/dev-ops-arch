from datetime import date, datetime
from domain.__shared.event.event_interface import EventInterface
from typing import Dict

class ProductCreatedEvent(EventInterface):
    data_time_occurred: date
    event_data: any

    def __init__(self, event_data: Dict):
        self.data_time_occurred = datetime.now()
        self.event_data = event_data