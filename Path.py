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
        calculation_point = self.nodes[0].position
        calculation_vector = Vector(Point(0, 0), Point(0, 0))
        """
        for count in range(precision):
            calculation_vector = Vector(Point(0, 0), Point(0, 0))
            for node in self.nodes[2:]:
                calculation_vector.add(node.position.multiply(Point(count, count)))

            vector_list.append(calculation_vector)
        """

        calculation_point = self.nodes[0].position
        calculation_vector = Vector(Point(0, 0), calculation_point)

        vector_list.append(
            calculation_vector
        )

        return vector_list

    """
    for _ in range(100):
        vector.components reset to 0
        
        for node in nodes:
            vector.components add with (node.position - vector.location multiply with "precision")
            
        vector.location add with vector.components
        
    """
