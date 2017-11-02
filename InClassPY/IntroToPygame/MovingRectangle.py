import pygame
import math
import time
pygame.init() ##starts pygame
black=[0,0,0] ##colors
red=[255,0,0]
green=[0,255,0]
blue=[0,0,255]
white=[255,255,255]
font=pygame.font.Font(None,25) ## Intitalzised the font for the file
pi=math.pi ##pi for drawing arcs

size=[400,400] ##screen size for pygame drawing

screen=pygame.display.set_mode(size) ##creates the screen

pygame.display.set_caption("My First Pygame Program")##displays text on the screen
rect_x=0
done=False
clock=pygame.time.Clock()
while done==False: ##Run loop of eventchecks
    clock.tick(10)
    ##Drawing happens here----------
    screen.fill(white) #Turns screen White
    pygame.draw.rect(screen,red,[rect_x,150,24,40],2)
    rect_x+=5
    pygame.display.flip()
    ##Drawing Ends here------------
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()##ends pygame to make it idlefriendly
