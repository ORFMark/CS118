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
screen.fill(white) #Turns screen White
pygame.display.set_caption("My First Pygame Program")##displays text on the screen

done=False
clock=pygame.time.Clock()
while done==False: ##Run loop of eventchecks
    clock.tick(10)
    ##Drawing happens here----------
    pygame.draw.line(screen,green,[0,0],[100,100],2) ##Draws a green line
    y_offset=0
    pygame.display.update()##Updates the display
    while y_offset<100: ##draws 10 parralell lines
        pygame.draw.line(screen,black,[0,10+y_offset],[100,100+y_offset],5)
        y_offset+=10
    text=font.render("My Text", True,black) ##sets up the text, redraw, and the color
    screen.blit(text,[150,150])##Writes the text
    rect1=pygame.draw.rect(screen,red,[250,250,20,40],2)#Draws a rectangle
    print(rect1.getX())
    pygame.draw.ellipse(screen,blue,[150,150,40,20],3) ##Draws an ellipse
    pygame.draw.arc(screen,green,[300,300,30,30],0,pi/2,3) ## draws and arck
    pygame.draw.arc(screen,blue,[300,300,30,30],pi/2,pi,3)
    pygame.draw.arc(screen,red,[300,300,30,30],pi,(3*pi)/2,3)
    pygame.draw.arc(screen,black,[300,300,30,30],(3*pi)/2,2*pi,3)
    pygame.display.update()
    ##Drawing Ends here------------
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()##ends pygame to make it idlefriendly
