import pygame
import math

pygame.init() ##starts pygame
black=[0,0,0] ##colors
red=[255,0,0]
green=[0,255,0]
blue=[0,0,255]
white=[255,255,255]
pi=math.pi ##pi for drawing arcs

size=[400,400] ##screen size for pygame drawing

screen=pygame.display.set_mode(size) ##creates the screen

pygame.display.set_caption("my first pygame program")##displays text on the screen

done=False
clock=pygame.time.Clock()
while done==False:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
pygame.quit()
        
    
