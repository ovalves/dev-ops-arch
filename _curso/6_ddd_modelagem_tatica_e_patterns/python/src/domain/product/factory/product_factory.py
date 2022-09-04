import uuid
from domain.product.entity.product import Product

class ProductFactory:
    @staticmethod
    def create(name: str, price: int) -> Product:
        return Product(str(uuid.uuid4()), name, price)