from typing import List
from domain.product.entity.product import Product

class ProductService:
    @staticmethod
    def increase_price(products: List[Product], percentage: int) -> List[Product]:
        for product in products:
            product.change_price((product.price * percentage) / 100 + product.price)

        return products