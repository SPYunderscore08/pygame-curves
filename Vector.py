from Point import *

class Vector:
    def __init__(self, components: Point):
        self.location_vector = components

    def add(self, vector: Point):
        self.location_vector.x += vector.x
        self.location_vector.y += vector.y

    def average(self, vector_list: list):
        sum_x = self.location_vector.x
        sum_y = self.location_vector.y

        for vector in vector_list:
            sum_x += vector.location_vector.x
            sum_y += vector.location_vector.y

        avg_x = sum_x /  len(vector_list) + 1
        avg_y = sum_y /  len(vector_list) + 1

        self.location_vector.x = avg_x
        self.location_vector.y = avg_y
