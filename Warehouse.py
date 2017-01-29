from _ast import List

from Point import Point
from Product import Product


class Warehouse:
    def __init__(self, position : Point, products : List[(Product, int)]):
        self.position, self.products = position, products