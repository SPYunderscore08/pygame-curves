from Point import *

class Vector:
    def __init__(self, components: Point):
        self.components = components

    def __copy__(self):
        return Vector(self.components.__copy__())
