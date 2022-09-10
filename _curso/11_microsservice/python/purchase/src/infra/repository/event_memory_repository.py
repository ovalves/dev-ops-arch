from typing import Any
from copy import deepcopy
from domain.repository.event_repository import EventRepository
from domain.entity.event import Event

class EventMemoryRepository(EventRepository):
    __memory = {}

    def __init__(self):
        self.__memory = {}

    def save(self, event: Event) -> Any:
        if event.code not in self.__memory:
            self.__memory[event.code] = []

        self.__memory[event.code].append(deepcopy(event))

    def get(self, code: str) -> Event:
        if code not in self.__memory:
            raise Exception('Event not found')

        return self.__memory[code][0]