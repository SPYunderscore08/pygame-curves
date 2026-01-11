from Point import *

class Node:
    def __init__(self, position: Point):
        self.position = position

    def move(self, new_position):
        self.position = new_position