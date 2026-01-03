import pygame
from Color import *

class Window:
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.screen.fill(WHITE)
        self.run()


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
