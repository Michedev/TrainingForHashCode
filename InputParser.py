from Product import *
from Warehouse import *
from Point import *

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

        self.products = []
        self.warehouses = []

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

    def readProducts(self, weightsLine):
        weights = weightsLine.split(" ")
        i = 0
        for w in weights:
            self.products.append(Product(i, w))
            i += 1


    def readWarehouses(self, file, num):
        for i in range(0, num):
            line = file.readline().split(" ")
            position = Point((int(line[0]), int(line[1])))
            availabilities = 
