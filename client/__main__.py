import pygame
from .settings import *
from .player import Player
from .udpserver_connection import UDPServerConnection
from server.settings import ADDR, PORT


pygame.init()

username = input("Enter username to join (4 characters max): ")
if username == "":
    print("Empty username!")
    exit()
elif len(username) > 4:
    print("Username too long!")
    exit()

conn = UDPServerConnection(ADDR, PORT)
player = conn.join(username)

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Multiplayer Cubes")

try:
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
except KeyboardInterrupt:
    pygame.quit()
    conn.leave(player)
    exit()

pygame.quit()
conn.leave(player)
