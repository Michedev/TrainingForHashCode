from typing import List

from Drone import Drone
from Order import Order
from Warehouse import Warehouse


def start(drones : List[Drone], orders : List[Order], warehouses : List[Warehouse], deadline : int):
    drone = drones[0]
    for tickOfTime in range(0, deadline):
        if not drone.isBusy:
            pass
