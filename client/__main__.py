import pygame 
import typing
import time

d_x = 800
d_y = 600
white = (255, 255, 255)



pygame.init()

display = pygame.display.set_mode((d_x, d_y))
pygame.display.set_caption("Multiplayer Cubes")

class Shape:

    # def __init__(self, posx, posy):
    #     self.posx = posx
    #     self.posy = posy


    def draw(self, display, color, posx, posy, length, width):
        self.length = length 
        self.width = width
        self.display = display
        self.color = color
        self.posx = posx
        self.posy = posy


        pygame.draw.rect(self.display, self.color, [self.posx, self.posy, self.length, self.width])
        
    
    # def move(self, distance):
    #     self.distance = distance
    #     key = pygame.key.get_pressed()
        
    #     if key[pygame.K_LEFT]:

    #         self.posx -= distance
    #     elif key[pygame.K_RIGHT]:
            
    #         self.posx += distance 
        
    #     elif key[pygame.K_UP]:

    #         self.posy -= distance 

    #     elif key[pygame.K_DOWN]:

    #         self.posy += distance
        
            
    
square = Shape()







run = True
while run: 
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    square.draw(display, white, 0, 0, 100, 100)
    key = pygame.key.get_pressed()
    distance = 5
        
    if key[pygame.K_LEFT]:

        square.posx -= distance
    elif key[pygame.K_RIGHT]:
            
        square.posx += distance 
        
    elif key[pygame.K_UP]:

        square.posy -= distance 

    elif key[pygame.K_DOWN]:

        square.posy += distance


    pygame.display.flip()
        
    

def main():
    setup()
    

if __name__ == '__main__':
    main() 
