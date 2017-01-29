from typing import List

from Point import Point
from Product import Product


class Order:
    def __init__(self, deliverPosition: Point, products: list[(Product, int)]):
        self.deliverPosition,  self.products, self.satisfied = deliverPosition, products, False
