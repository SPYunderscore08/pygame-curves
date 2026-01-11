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

    def draw_path(self, path: Path):
        line_list = path.calculate_path(100)

        self.screen.fill(BlACK)

        pygame.draw.rect(self.screen, RED, path.start.position.to_tuple() + (path.node_vicinity, path.node_vicinity))
        pygame.draw.rect(self.screen, RED, path.end.position.to_tuple() + (path.node_vicinity, path.node_vicinity))
        for node in path.nodes:
            pygame.draw.rect(self.screen, BLUE, node.position.to_tuple() + (path.node_vicinity, path.node_vicinity))

        for line in line_list:
            pass
            #pygame.draw.line(self.screen, WHITE, line[0], line[1], 1)

        pygame.display.flip()

