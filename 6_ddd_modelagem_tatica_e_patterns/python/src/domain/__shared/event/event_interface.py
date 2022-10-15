from datetime import date
from abc import ABC
from typing import Any

class EventInterface(ABC):
    dataTimeOccurred: date
    eventData: Any
