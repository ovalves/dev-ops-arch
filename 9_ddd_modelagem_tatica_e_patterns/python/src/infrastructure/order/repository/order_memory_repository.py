from typing import Any
from copy import deepcopy

class OrderMemoryRepository:
    __memory = {}

    def __init__(self):
        self.__memory = {}

    async def create(self, entity: any) -> Any:
        if entity.id not in self.__memory:
            self.__memory[entity.id] = []

        self.__memory[entity.id].append(deepcopy(entity))

    async def find(self, id: str) -> Any:
        if id not in self.__memory:
            raise Exception('Order not found')

        return self.__memory[id][0]