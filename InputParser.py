from Product import *
from Warehouse import *
from Point import *
from collections import Counter
from Order import *
from Drone import *


class InputParser:
    def __init__(self):
        self.inputPath = "InputData/"
        self.numberOfRows = 0
        self.numberOfColumns = 0
        self.numberOfDrones = 0
        self.deadline = 0
        self.maxLoad = 0
        self.numberOfProducts = 0
        self.numberOfWarehouses = 0
        self.numberOfOrders = 0

        self.products = []
        self.warehouses = []
        self.orders = []
        self.drones = []

    def loadInput(self, fileName):
        file = open(self.inputPath+fileName)

        firstLine = file.readline().split(" ")
        self.numberOfRows = int(firstLine[0])
        self.numberOfColumns = int(firstLine[1])
        self.numberOfDrones = int(firstLine[2])
        self.deadline = int(firstLine[3])
        self.maxLoad = int(firstLine[4])

        self.numberOfProducts = int(file.readline())
        self.readProducts(file.readline())

        self.numberOfWarehouses = int(file.readline())
        self.readWarehouses(file, self.numberOfWarehouses)

        self.numberOfOrders = int(file.readline())
        self.readOrders(file, self.numberOfOrders)

        startingPosition = Point((0,0))
        for i in range(0, self.numberOfDrones):
            self.drones.append(Drone(self.maxLoad, startingPosition))

    def readOrders(self, file, num):
        for i in range(0, num):
            line = file.readline().split(" ")
            position = Point((int(line[0]), int(line[1])))
            numberOfProducts = int(file.readline())

            countedProducts = Counter(list(map(lambda el : int(el), file.readline().split(" "))))

            j = 0
            products = []
            for cP in countedProducts:
                products.append((self.products[cP], countedProducts[cP]))
                j += 1
            self.orders = Order(position, products)


    def readProducts(self, weightsLine):
        weights = weightsLine.split(" ")
        i = 0
        for w in weights:
            self.products.append(Product(i, int(w)))
            i += 1

    def readWarehouses(self, file, num):
        for i in range(0, num):
            line = file.readline().split(" ")
            position = Point((int(line[0]), int(line[1])))
            availabilities = file.readline().split(" ")

            j = 0
            warehouseProductList = []
            for a in availabilities:
                warehouseProductList.append((self.products[j], int(a)))
                j += 1
            self.warehouses.append(Warehouse(position, warehouseProductList))

