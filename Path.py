import pygame.draw

from Vector import *

class Path:
    def __init__(self, start: Point, end: Point, control_points: list[Point]):
        self.start = start
        self.end = end
        self.control_points = control_points

    def calculate_path(self) -> list:
        start_to_end_x = self.end.x - self.start.x
        start_to_end_y = self.end.y - self.start.y
        calculation_vector = Vector(Point(start_to_end_x, start_to_end_y), self.start)
        line_list = []
        i = 0
        while i < 10:#calculation_vector.location != self.end:
            print(calculation_vector.components.x)
            print(calculation_vector.components.y)
            print()
            new_x = self.end.x - calculation_vector.location.x
            new_y = self.end.y - calculation_vector.location.y
            calculation_vector.components = Point(new_x, new_y)

            for point in self.control_points:
                calculation_vector.add(Point(point.x - calculation_vector.location.x, point.y - calculation_vector.location.y))

            line_list.append((calculation_vector.location.to_tuple(), calculation_vector.components.to_tuple()))
            calculation_vector.location = calculation_vector.components
            i += 1

        return line_list
