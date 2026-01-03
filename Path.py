from Vector import *

class Path:
    def __init__(self, start: Point, end: Point, control_points: list[Point]):
        self.start = start
        self.end = end
        self.control_points = control_points

    def calculate_path(self) -> list:
        start_to_end_x = self.end.x - self.start.x
        start_to_end_y = self.end.y - self.start.y
        starting_vector = Vector(Point(start_to_end_x, start_to_end_y))
        calculation_vector = Vector(starting_vector.components)
        line_list = []
        i = 0
        while i < 10:
            for point in self.control_points:
                calculation_vector.add(point)
            line_list.append((starting_vector.components.to_tuple(), calculation_vector.components.to_tuple()))
            starting_vector = calculation_vector
            i += 1

        return line_list
