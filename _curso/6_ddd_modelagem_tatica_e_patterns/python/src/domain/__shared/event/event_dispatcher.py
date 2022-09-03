from typing import Dict
from domain.__shared.event.event_dispatcher_interface import EventDispatcherInterface
from domain.__shared.event.event_handler_interface import EventHandlerInterface
from domain.__shared.event.event_interface import EventInterface


class EventDispatcher(EventDispatcherInterface):
    __event_handlers: Dict[str, EventHandlerInterface] = {}

    def __init__(self):
        self.__event_handlers = {}

    def get_event_handlers(self) -> Dict[str, EventHandlerInterface]:
        return self.__event_handlers

    def notify(self, event: EventInterface) -> None:
        event_name = event.__class__.__name__
        if event_name in self.__event_handlers:
            for event_handler in self.__event_handlers[event_name]:
                event_handler.handle(event)

    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        if event_name not in self.__event_handlers:
            self.__event_handlers[event_name] = []

        self.__event_handlers[event_name].append(event_handler)

    def unregister(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        if event_name in self.__event_handlers:
            index = self.__event_handlers[event_name].index(event_handler)
            if index != -1:
                del self.__event_handlers[event_name][index]

    def unregister_all(self) -> None:
        self.__event_handlers = {}