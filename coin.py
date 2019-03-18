from math import sqrt


class Coin:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def intersect(self, other):
        distance_between = sqrt((self.center[0] - other.center[0]) ** 2 + (self.center[1] - other.center[1]) ** 2)
        return distance_between < (self.radius + other.radius)
