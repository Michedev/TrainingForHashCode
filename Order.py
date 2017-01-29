from typing import List, Tuple

from Point import Point
from Product import Product


class Order:
    def __init__(self, deliverPosition: Point, products: List[Tuple[Product, int]]):
        self.deliverPosition,  self.products, self.satisfied = deliverPosition, products, False
