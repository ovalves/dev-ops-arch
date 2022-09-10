from typing import Callable
from abc import ABC, abstractmethod

class HttpServer(ABC):
    @abstractmethod
    def on(self, method: str, url: str, callback: Callable) -> None:
        pass

    @abstractmethod
    def listen(self, port: int) -> None:
        pass
