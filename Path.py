from Vector import *
from Node import *

class Path:
    def __init__(self, start: Node, end: Node, node_vicinity):
        self.start = start
        self.end = end
        self.node_vicinity = node_vicinity
        self.nodes = [self.start, self.end]

    def calculate_path(self, precision: int) -> list: # percentual change; ratio is the parameter
        start_to_end_x = self.end.position.x - self.start.position.x
        start_to_end_y = self.end.position.y - self.start.position.y
        calculation_vector = Vector(Point(start_to_end_x * precision, start_to_end_y * precision), self.start.position)

        line_list = []

        precision_counter = 0

        while precision_counter < precision:

            for node in self.nodes:
                calculation_vector.add(Point((node.position.x - calculation_vector.location.x) * precision, (node.position.y - calculation_vector.location.y) * precision))

            calculation_vector.add(Point(precision, precision))

            line_list.append(
                (
                    calculation_vector.location.to_tuple(),
                    calculation_vector.components.to_tuple()
                )
            )

            calculation_vector.location = calculation_vector.components
            precision_counter += 1

        return line_list
