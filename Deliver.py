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
            if len(orders) <= currentOrder:
                return True
            if not drone.isBusy:
                order = orders[currentOrder]
                self.satisfyOrder(order, drone, warehouses)
                currentOrder += 1
            else:
                drone.busyTime -= 1
                if drone.busyTime == 0:
                    drone.isBusy = False

    def satisfyOrder(self, order: Order, drone: Drone, warehouses: List[Warehouse]):
        drone.isBusy = True
        for product in order.products:
            if product[1] == 0:
                continue
            if order.satisfied:
                break
            choosedWarehouse = self.searchWarehousesByProduct(warehouses, product)
            if choosedWarehouse is None:
                return False

            choosedWarehouse.take(product[0].type, product[1])
            drone.loadItem(product)
            drone.busyTime += drone.position.distance(choosedWarehouse.position) + 1
            self.commands += str(drone.id) + " L " + str(choosedWarehouse.id) + " " + str(product[0].type) + " " + str(product[1]) + "\n"
            drone.position = choosedWarehouse.position

            drone.busyTime += drone.position.distance(order.deliverPosition) + 1
            self.commands += str(drone.id) + " D " + str(order.id) + " " + str(product[0].type) + " " + str(product[1])+ "\n"
            drone.position = order.deliverPosition

            order.deliver([product])
            drone.unloadItem(product)

        return order.satisfied



    def searchWarehousesByProduct(self, warehouses : List[Warehouse], product : Tuple[Product, int]):
        availableWarehouses = list(filter(lambda el : el.products[product[0].type][1] > 0 , warehouses))
        maxWarehouseByProductQuantity = max(availableWarehouses, key=lambda el : el.products[product[0].type][1])
        if maxWarehouseByProductQuantity.products[product[0].type][1] >= product[1]:
            return maxWarehouseByProductQuantity
        return None
