from functools import reduce
from typing import List, Tuple

from Point import Point
from Product import Product


class Warehouse:
    def __init__(self, position : Point, products : List[Tuple[Product, int]]):
        self.position, self.products = position, products
        self.products.sort(key= lambda pair : pair[0].type)
    def quantityOf(self, productType : int) -> int:
        return reduce(lambda q1, q2 : q1 + q2, map(lambda pair: pair[1] ,filter(lambda pair : pair[0].type == productType, self.products)))
    def take(self, productType : int, quantityToTake : int):
        actualQuantity = self.quantityOf(productType)
        assert(actualQuantity >= quantityToTake)
        self.products[productType] = (self.products[productType][0], actualQuantity - quantityToTake)

