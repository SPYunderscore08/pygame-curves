import pygame
from pygame.draw_py import draw_line

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

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def draw_path(self, path: Path):
        line_list = path.calculate_path()
        for line in line_list:
            print(line)
            pygame.draw.line(self.screen, WHITE, line[0], line[1], 1)
            pygame.display.flip()
