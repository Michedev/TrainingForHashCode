from functools import reduce

from Point import Point
from Product import Product


class Warehouse:
    def __init__(self, position : Point, products : list[(Product, int)]):
        self.position, self.products = position, products
    def quantityOf(self, productType : int) -> int:
        return reduce(lambda q1, q2 : q1 + q2, map(lambda pair: pair[1] ,filter(lambda pair : pair[0].type == productType, self.products)))