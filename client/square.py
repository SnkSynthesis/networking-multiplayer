import pygame
from .settings import *
from typing import Any


class Square:
    def __init__(self, posx: int, posy: int, color: Any) -> None:
        self.posx = posx
        self.posy = posy
        self.color = color

    def draw(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(
            surface, self.color, (self.posx, self.posy, SQUARE_WIDTH, SQUARE_WIDTH)
        )
