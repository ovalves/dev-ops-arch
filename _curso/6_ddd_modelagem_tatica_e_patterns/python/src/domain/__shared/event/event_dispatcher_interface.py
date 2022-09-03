from abc import ABC, abstractmethod
from typing import Dict
from domain.__shared.event.event_interface import EventInterface
from domain.__shared.event.event_handler_interface import EventHandlerInterface

class EventDispatcherInterface(ABC):
    @abstractmethod
    def get_event_handlers(self) -> Dict[str, EventHandlerInterface]:
        pass

    @abstractmethod
    def notify(self, event: EventInterface) -> None:
        pass

    @abstractmethod
    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        pass

    @abstractmethod
    def unregister(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        pass

    @abstractmethod
    def unregister_all(self) -> None:
        pass