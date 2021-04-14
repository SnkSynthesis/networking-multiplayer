import pygame
from .settings import *
from .square import Square


class Player(Square):
    def __init__(self) -> None:
        super().__init__(100, 100, PLAYER_COLOR)

    def check_collision(self) -> None:
        # Check if it collides with borders (X-Axis)
        if self.posx > DISPLAY_WIDTH - SQUARE_WIDTH:
            self.posx = DISPLAY_WIDTH - SQUARE_WIDTH
        elif self.posx < 0:
            self.posx = 0

        # Check if it collides with borders (Y-Axis)
        if self.posy > DISPLAY_HEIGHT - SQUARE_WIDTH:
            self.posy = DISPLAY_HEIGHT - SQUARE_WIDTH
        elif self.posy < 0:
            self.posy = 0

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.posx -= PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.posx += PLAYER_SPEED

        if keys[pygame.K_UP]:
            self.posy -= PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            self.posy += PLAYER_SPEED
