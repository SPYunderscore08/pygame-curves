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
        dragging_node = None
        last_node = None

        pygame.time.wait(10)
        self.window.draw_path(self.path)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_dragging = True
                    dragging_node = self.alter_simulation()

                if event.type == pygame.MOUSEBUTTONUP:
                    is_dragging = False
                    dragging_node = None

            if dragging_node is None and last_node is not None:
                print("test")
                self.window.draw_path(self.path)
                last_node = None

            if is_dragging:
                self.drag_node(dragging_node)
                last_node = dragging_node

            #pygame.time.wait(20) # todo, maybe keep for performance


    def start(self):
        t1 = threading.Thread(target=self.window.run)
        t2 = threading.Thread(target=self.run_event_loop)
        t1.start()
        t2.start()


    def alter_simulation(self): # todo make better & rename
        position = Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        for node in self.path.nodes:
            tmp_point = node.position.subtract(position)
            if abs(tmp_point.x) <= self.path.node_vicinity // 2 and abs(tmp_point.y) <= self.path.node_vicinity // 2:
       #         node.position = position
                return node
        return None


    def drag_node(self, node: Node):
        if not node is None:
            print("test")
            self.window.draw_path(self.path, node)
            node.position = Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
