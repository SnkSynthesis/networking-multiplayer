import pygame 

def setup():
    pygame.init()
    display = pygame.display.set_mode((1000, 1000))

class Object:

    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 

cube = Object()

def main():
    setup()

if __name__ == '__main__':
    main()