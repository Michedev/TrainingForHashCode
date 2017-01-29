from typing import Tuple
from Product import Product
from Point import Point


class Drone:
    id = 0

    def __init__(self, maxWeight : int, position : Point):
        self.maxWeight = maxWeight
        self.position = position
        self.currentWeight = 0
        self.loadedItems = []
        self.isBusy = False
        self.id = Drone.id
        Drone.id += 1

    def loadItem(self, productWithQty : Tuple[Product, int]):
        self.loadedItems.append(productWithQty)
        productsWeight = productWithQty[0].weight * productWithQty[1]
        self.currentWeight += productsWeight

        assert(self.currentWeight <= self.maxWeight)

    def unloadItem(self, productWithQty : Tuple[Product, int]):
        itemToUnload = list(filter(lambda el : el[0].type == productWithQty[0].type, self.loadedItems))
        self.loadedItems.remove(itemToUnload)
        productsWeight = productWithQty[0].weight * productWithQty[1]
        self.currentWeight -= productsWeight

        assert(self.currentWeight >= 0)

    def checkProductWeight(self, productWithQty : Tuple[Product, int]):
        productsWeight = productWithQty[0].weight * productWithQty[1]
        return productsWeight + self.currentWeight <= self.maxWeight