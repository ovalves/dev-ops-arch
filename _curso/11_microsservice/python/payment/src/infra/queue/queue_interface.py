from abc import ABC, abstractmethod
from typing import Any, Callable


class QueueInterface(ABC):
    @abstractmethod
    def connect(self) -> Any:
        pass

    @abstractmethod
    def close(self) -> Any:
        pass

    @abstractmethod
    def consume(self, event_name: str, callback: Callable) -> Any:
        pass

    @abstractmethod
    def publish(self, event_name: str, data: Any) -> Any:
        pass
