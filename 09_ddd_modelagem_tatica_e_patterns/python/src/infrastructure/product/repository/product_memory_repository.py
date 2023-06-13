from typing import Any
from copy import deepcopy
from domain.product.repository.product_repository_interface import ProductRepositoryInterface

class ProductMemoryRepository(ProductRepositoryInterface):
    __memory = {}

    def __init__(self):
        self.__memory = {}

    async def create(self, entity: any) -> Any:
        if entity.id not in self.__memory:
            self.__memory[entity.id] = []

        self.__memory[entity.id].append(deepcopy(entity))

    async def update(self, entity: any) -> Any:
        try:
            self.__memory.pop(entity.id, None)
            await self.create(entity)
        except Exception:
            raise Exception('Could not update entity')

    async def find(self, id: str) -> Any:
        if id not in self.__memory:
            raise Exception('Customer not found')

        return self.__memory[id][0]

    async def find_all(self) -> Any:
        return self.__memory.values()