import pygame
from .settings import *
from .player import Player


pygame.init()

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Multiplayer Cubes")

player = Player()

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    player.move()
    player.check_collision()

    display.fill(BG_COLOR)
    player.draw(display)
    pygame.display.update()

pygame.quit()
