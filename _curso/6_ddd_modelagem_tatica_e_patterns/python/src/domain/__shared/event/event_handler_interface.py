from abc import ABC, abstractmethod

class EventHandlerInterface(ABC):
    @abstractmethod
    def handle(self, event: any) -> None:
        pass