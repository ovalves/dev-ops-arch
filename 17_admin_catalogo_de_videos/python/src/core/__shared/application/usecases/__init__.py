import abc
from abc import ABC
from typing import Generic
from src.core.__shared.domain.types import Input, Output


class UseCase(Generic[Input, Output], ABC):
    @abc.abstractmethod
    def execute(self, input_param: Input) -> Output:
        raise NotImplementedError()
