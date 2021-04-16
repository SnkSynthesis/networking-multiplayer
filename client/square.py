import pygame
from .settings import *
from typing import Any
from dataclasses import dataclass


@dataclass
class Square:
    posx: int
    posy: int
    color: Any

    def draw(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(
            surface, self.color, (self.posx, self.posy, SQUARE_WIDTH, SQUARE_WIDTH)
        )
