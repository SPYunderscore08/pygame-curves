from PositionalVector import *
from Vector import *
from Node import *
from math import cos, pi

class Path:
    def __init__(self, start: Node, end: Node, node_vicinity):
        self.start = start
        self.end = end
        self.node_vicinity = node_vicinity
        self.nodes = [self.start, self.end]

    def calculate_path(self, precision: float) -> list: # percentual change; ratio is the parameter
        vector_list = []

        calculation_point = self.nodes[0].position.__copy__()
        calculation_vector = PositionalVector(Vector(Point(0, 0)), calculation_point)

        mid_point = (self.nodes[0].position.__copy__().add(self.nodes[-1].position)).divide(Point(2, 2))

        for node in self.nodes:
            #vector_list.append(calculation_vector.__copy__())
            vector_list.append(
                PositionalVector(
                    mid_point.__copy__().subtract(node.position),
                    mid_point
                )
            )


        return vector_list
