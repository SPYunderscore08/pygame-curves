from Point import *

class Vector:
    def __init__(self, components: Point, location=Point(0, 0)):
        self.components = components
        self.location = location

    def add(self, vector: Point):
        self.components.x += vector.x
        self.components.y += vector.y

    def average(self, vector_list: list):
        sum_x = self.components.x
        sum_y = self.components.y

        for vector in vector_list:
            sum_x += vector.components.x
            sum_y += vector.components.y

        avg_x = sum_x / (len(vector_list) + 1)
        avg_y = sum_y / (len(vector_list) + 1)

        self.components.x = avg_x
        self.components.y = avg_y