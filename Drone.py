from Point import Point


class Drone:
    def __init__(self, maxWeight : int, position : Point):
        self.maxWeight = maxWeight
        self.position = position