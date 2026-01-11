import pygame
import threading

from Window import *
from Path import *
from Vector import *
from Path import *
from Color import *
from Node import *

class Simulation:
    def __init__(self, width: int, height: int, title: str, start: Node, end: Node, node_vicinity: int):
        self.window = Window(width, height, title)
        self.path = Path(start, end, node_vicinity)


    def run_event_loop(self):
        running = True
        is_dragging = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_dragging = True
                if event.type == pygame.MOUSEBUTTONUP:
                    is_dragging = False

            if is_dragging:
                self.alter_simulation()

    def start(self):
        t1 = threading.Thread(target=self.window.run)
        t2 = threading.Thread(target=self.run_event_loop)
        t1.start()
        t2.start()


    def alter_simulation(self):
        position = Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        for node in self.path.nodes:
            print("node:", type(node))
            print("node.position:", type(node.position), node.position)
            tmp_point = node.position.subtract(position)
            print("tmp_point:", type(tmp_point), tmp_point.to_tuple())
            if abs(tmp_point.x) <= self.path.node_vicinity and abs(tmp_point.y) <= self.path.node_vicinity:
                node.position = position

        self.window.draw_path(self.path)
