from Vector import *
from Point import *

class PositionalVector:
    def __init__(self, vector: Vector, location: Point):
        self.vector = vector
        self.location = location

    def __copy__(self):
        return PositionalVector(
            self.vector.__copy__(),
            self.location.__copy__()
        )