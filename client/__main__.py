import pygame 
<<<<<<< HEAD

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
=======
import typing
import time

d_x = 800
d_y = 600
white = (255, 255, 255)


def setup():
    pygame.init()

display = pygame.display.set_mode((d_x, d_y))
pygame.display.set_caption("Multiplayer Cubes")

class Shape:

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy


    def draw(self, display, color, posx, posy, length, width):
        self.length = length 
        self.width = width
        self.display = display
        self.color = color
        # self.posx = posx
        # self.posy = posy

        pygame.draw.rect(self.display, self.color, [self.posx, self.posy, self.length, self.width])
    
    def move(self, x, y):
        self.x = x   
        self.y = y 
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT]:
            
            self.x -= distance
        elif key[pygame.K_RIGHT]:
            
            x += distance 
        
        elif key[pygame.K_UP]:

            y -= distance 

        elif key[pygame.K_DOWN]:

            y += distance
        
            
    
square = Shape(0, 0)
square.draw(display, white, 0, 0, 100, 100)

square.move(0, 0)

pygame.display.flip()



def run():
    run = True
    while run == True: 
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()


def main():
    setup()
    run()

if __name__ == '__main__':
    main() 
>>>>>>> 92b0267a149dcfdce9e93aec0c8288a6f8ec7b89
