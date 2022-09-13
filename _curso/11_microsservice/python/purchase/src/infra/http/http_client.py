from typing import Any
from abc import ABC, abstractmethod


class HttpClient(ABC):
    @abstractmethod
    def get(self, url: str) -> Any:
        pass

    @abstractmethod
    def post(self, url: str, data: Any) -> Any:
        pass
