from Vector import *
from Node import *

class Path:
    def __init__(self, start: Node, end: Node, node_vicinity):
        self.start = start
        self.end = end
        self.node_vicinity = node_vicinity
        self.nodes = [self.start, self.end]

    def calculate_path(self, precision: float) -> list: # percentual change; ratio is the parameter
        percent_per_node = len(self.nodes) - 1
        vector_list = []
        forces = [] * percent_per_node

        calculation_point = self.nodes[0].position.__copy__()
        calculation_vector = Vector(calculation_point, calculation_point)

        for node in self.nodes:
            #mid_point = Vector.calculate_midpoint(calculation_vector)

            vector_list.append(calculation_vector.__copy__())

            vector_list.append(
                Vector(
                    node.position,
                    Vector.calculate_midpoint(Vector(self.nodes[-1].position, self.nodes[0].position))
                )
            )

            calculation_vector.components = calculation_point.__copy__()

        return vector_list
