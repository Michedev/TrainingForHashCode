import math

class Point:
    def __init__(self, position : (int, int)):
        self.x = position[0]
        self.y = position[1]

    def distance(self, otherPoint):
        d = (abs(self.x - otherPoint.x)**2 + abs(self.y - otherPoint.y)**2)**(1/2)
        return math.ceil(d)
