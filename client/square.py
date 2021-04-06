import pygame
from .settings import *


class Square:
    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(
            surface, self.color, (self.posx, self.posy, SQUARE_WIDTH, SQUARE_WIDTH)
        )