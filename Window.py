import pygame

from Color import *
from Path import *

class Window:
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title
        self.screen = None

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(BlACK)

    def draw_path(self, path: Path, highlight_node = None):
        line_list = path.calculate_path(100)

        vicinity_point = Point(path.node_vicinity, path.node_vicinity).divide(Point(2, 2))
        vicinity_tuple = (path.node_vicinity, path.node_vicinity)

        self.screen.fill(BlACK)

        pygame.draw.rect(
            self.screen,
            GREEN,
            path.start.position.subtract(vicinity_point, True).to_tuple() + vicinity_tuple
        )

        pygame.draw.rect(
            self.screen,
            RED,
            path.end.position.subtract(vicinity_point, True).to_tuple() + vicinity_tuple
        )

        for node in path.nodes[1:-1]:
            pygame.draw.rect(
                self.screen,
                BLUE,
                node.position.subtract(vicinity_point, True).to_tuple() + vicinity_tuple
            )

        for line in line_list:
            pygame.draw.line(self.screen, WHITE, line.location.to_tuple(), line.location.__copy__().subtract(line.vector).to_tuple(), 1)


        #mouse_pos = pygame.mouse.get_pos()
        #for node in path.nodes[:-1]:
        #    pygame.draw.line(self.screen, BLUE, node.position.to_tuple(), (mouse_pos[0], node.position.to_tuple()[1]))
        #    pygame.draw.line(self.screen, RED, node.position.to_tuple(), (node.position.to_tuple()[0], mouse_pos[1]))



        if highlight_node is not None:
            pygame.draw.rect(
                self.screen,
                WHITE,
                highlight_node.position.subtract(
                    vicinity_point.add(Point(5, 5)), True
                ).to_tuple() + (path.node_vicinity + 10, path.node_vicinity + 10),
                2
            )

        pygame.display.flip()
