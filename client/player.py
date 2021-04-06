import pygame
from .settings import *
from .square import Square


class Player(Square):
    def __init__(self):
        super().__init__(100, 100, (255, 0, 0))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.posx -= PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.posx += PLAYER_SPEED

        if keys[pygame.K_UP]:
            self.posy -= PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            self.posy += PLAYER_SPEED