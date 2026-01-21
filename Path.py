from Vector import *
from Node import *

class Path:
    def __init__(self, start: Node, end: Node, node_vicinity):
        self.start = start
        self.end = end
        self.node_vicinity = node_vicinity
        self.nodes = [self.start, self.end]

    def calculate_path(self, precision: float) -> list: # percentual change; ratio is the parameter
        vector_list = []

        calculation_point = self.nodes[0].position.__copy__()
        calculation_vector = Vector(calculation_point, calculation_point)

        default_vector = Vector(self.nodes[-1].position, calculation_point)
        mid_point = Vector.calculate_midpoint(default_vector)

        for node in self.nodes:


            #region visualisation
            vector_list.append(calculation_vector.__copy__())
            vector_list.append(
                Vector(
                    node.position,
                    mid_point
                )
            )
            #endregion visualisation

            calculation_vector.components = calculation_point.__copy__()



        calculation_point = self.nodes[0].position.__copy__()
        calculation_vector = Vector(Point(0, 0), calculation_point)

        mid_point = Vector.calculate_midpoint(Vector(self.nodes[0].position, self.nodes[-1].position))

        x_vector = Vector(Point(0, 0))
        y_vector = Vector(Point(0, 0))

        for node in self.nodes[1:-1]:
            calculation_point.add(calculation_vector.components)
            calculation_vector.location = calculation_point


        return vector_list


