from typing import Callable
from abc import ABC, abstractmethod


class HttpServer(ABC):
    @abstractmethod
    def listen(self, port: int) -> None:
        pass
