from math import sqrt


class Table:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def surrounds(self, other):
        distance_between = sqrt((self.center[0] - other.center[0]) ** 2 + (self.center[1] - other.center[1]) ** 2)
        return self.radius >= distance_between + other.radius
