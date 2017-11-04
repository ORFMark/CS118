##Hey Ashish, Everything Runs
import pygame
import math
import random
pygame.init()
black=[0,0,0] ##colors
red=[255,0,0]
green=[0,255,0]
blue=[0,0,255]
white=[255,255,255]
yellow=[255,255,0]
purple=[255,0,255]
pi=math.pi
size=[700,400]
x_vector=[]
y_vector=[]
x=[]
y=[]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("MRB_Assignment7")
for i in range (0,10):
    x_vector.append(random.randint(-10,10))
    y_vector.append(random.randint(-10,10))
    x.append(random.randint(40,660))
    y.append(random.randint(40,340))
clock=pygame.time.Clock()
x_vector_init=x_vector.copy()
y_vector_init=y_vector.copy()
screen.fill(purple)
done=False
while done==False:
    clock.tick(10)
    screen.fill(purple)
    for j in range(0,5):
        x[j]=x[j]+x_vector[j]
        y[j]=y[j]+y_vector[j]
        if x[j]>680 or x[j]<10 or y[j]>380 or y[j]<10:
            x[j]=350
            y[j]=200
            x_vector[j]=random.randint(-10,10)
            y_vector[j]=random.randint(-10,10)
        if x_vector[j]==0 and y_vector[j]==0:
            x_vector[j]=random.randint(-10,10)
            y_vector[j]=random.randint(-10,10)
        pygame.draw.rect(screen,blue,[x[j],y[j],20,20])
    for j in range(5,10):
        x[j]=x[j]+x_vector[j]
        y[j]=y[j]+y_vector[j]
        if x[j]>680 or x[j]<20:
            x_vector[j]=-1*x_vector[j]
        if y[j]>380 or y[j]<20:
            y_vector[j]=-1*y_vector[j]
        pygame.draw.circle(screen,red,[x[j],y[j]],10)
    pygame.display.flip()
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()##ends pygame to make it idlefriendly
