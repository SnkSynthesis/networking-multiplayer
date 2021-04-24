import pygame
from .settings import *
from typing import Any
from dataclasses import dataclass


@dataclass
class Square:
    username: str
    posx: int
    posy: int
    color: Any

    def draw(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(
            surface, self.color, (self.posx, self.posy, SQUARE_WIDTH, SQUARE_WIDTH)
        )

        # From https://stackoverflow.com/a/3943023 but the original 186 is lowered to 161
        if self.color[0] * 0.299 + self.color[1] * 0.587 + self.color[2] * 0.114 > 161:
            img = FONT.render(self.username, True, (0, 0, 0))
        else:
            img = FONT.render(self.username, True, (255, 255, 255))

        surface.blit(
            img,
            (
                self.posx + SQUARE_WIDTH / 2 - img.get_width() / 2,
                self.posy + SQUARE_WIDTH / 2 - img.get_height() / 2,
            ),
        )
