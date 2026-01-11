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

        self.screen.fill(BlACK)

        pygame.draw.rect(self.screen, RED, path.start.position.subtract(
            Point(path.node_vicinity / 2, path.node_vicinity / 2)
        ).to_tuple() + (path.node_vicinity, path.node_vicinity))

        pygame.draw.rect(self.screen, RED, path.end.position.subtract(
            Point(path.node_vicinity / 2, path.node_vicinity / 2)
        ).to_tuple() + (path.node_vicinity, path.node_vicinity))

        for node in path.nodes[2:]:
            pygame.draw.rect(self.screen, BLUE, node.position.subtract(
                Point(path.node_vicinity / 2, path.node_vicinity / 2)
            ).to_tuple() + (path.node_vicinity, path.node_vicinity))

        for line in line_list:
            pass
            #pygame.draw.line(self.screen, WHITE, line[0], line[1], 1)
        if highlight_node is not None:
            pygame.draw.rect(self.screen, WHITE, highlight_node.position.subtract(
                Point(path.node_vicinity / 2 + 5, path.node_vicinity / 2 + 5)
            ).to_tuple() + (path.node_vicinity + 10, path.node_vicinity + 10), 2)

        pygame.display.flip()
