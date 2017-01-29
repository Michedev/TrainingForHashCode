from typing import List, Tuple

from Drone import Drone
from Order import Order
from Warehouse import Warehouse
from Product import Product

class DeliveryGuy:

    def __init__(self):
        self.commands = ""

    def start(self, drones : List[Drone], orders : List[Order], warehouses : List[Warehouse], deadline : int):
        drone = drones[0]
        currentOrder = 0

        for tickOfTime in range(0, deadline):
            if not drone.isBusy:
                order = orders[currentOrder]

    def satisfyOrder(self, order: Order, drone: Drone, warehouses: List[Warehouse]):
        choosedWarehouse = None
        for product in order.products:
            choosedWarehouse = self.searchWarehousesByProduct(warehouses, product)
            if choosedWarehouse is None:
                return False

            choosedWarehouse.take(product[0].type, product[1])
            drone.loadItem(product)
            self.commands += drone.id + " L " + choosedWarehouse.id + " " + product[0].type + " " + product[1]



    def searchWarehousesByProduct(self, warehouses : List[Warehouse], product : Tuple[Product, int]):
        availableWarehouses = list(filter(lambda el : el.products[product[0].type][1] > 0 , warehouses))
        maxWarehouseByProductQuantity = max(availableWarehouses, key=lambda el : el.products[product[0].type][1])
        if maxWarehouseByProductQuantity.products[product[0].type][1] >= product[1]:
            return maxWarehouseByProductQuantity
        return None