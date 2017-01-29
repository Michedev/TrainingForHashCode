from typing import List, Tuple

from Point import Point
from Product import Product


class Order:
    id = 0
    def __init__(self, deliverPosition: Point, products: List[Tuple[Product, int]]):
        self.deliverPosition,  self.products, self.satisfied = deliverPosition, products, False
        self.id = Order.id
        Order.id += 1

    def deliver(self, products : List[Tuple[Product, int]]):
        for product in products:
            orderProduct = self.findProduct(product[0].type)
            remainingItemToDelivery = orderProduct[1] - product[1]
            assert(remainingItemToDelivery >= 0)
            self.products.remove(orderProduct)
            self.products.append((orderProduct[0], remainingItemToDelivery))
        self.satisfied = self.isSatisfied()

    def findProduct(self, idProduct) -> Tuple[Product, int]:
        singleProduct = list(filter(lambda product : product[0].type == idProduct, self.products))
        assert(len(singleProduct) == 1)
        return singleProduct[0]

    def isSatisfied(self)-> bool:
        for product in self.products:
            if product[1] != 0:
                return False
        return True