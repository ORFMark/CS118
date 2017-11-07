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
size=[800,800]
pos_list=[]
vectorList=[]
sizeList=[]
countList=[]
count=0
for i in range (0,300):
    x=random.randint(1,800)
    y=random.randint(0,700)
    pos_list.append([x,y])
    countList.append([x,0])
screen=pygame.display.set_mode(size)
screen.fill(purple)
pygame.display.set_caption("Snow")
for i in range (0,len(pos_list)):
   vectorList.append(random.randint(3,10))
   sizeList.append(random.randint(2,5))
clock=pygame.time.Clock()

done=False
while done==False:
    clock.tick(30)
    screen.fill(blue)
    for i in range (len(pos_list)):
        if pos_list[i][1]>800:
            countList[i][1]=countList[i][1]+(sizeList[i]/2)
            count=count+.004
            pos_list[i][1]=random.randint(-20,-10)
            sizeList[i]=random.randint(2,5)
            vectorList[i]=random.randint(3,10)
        pygame.draw.circle(screen,white,pos_list[i],sizeList[i])
        pos_list[i][1]=pos_list[i][1]+vectorList[i]
        pygame.draw.rect(screen,white,[0,800-int(count),800,int(count)])
        pygame.draw.ellipse(screen,white,[countList[i][0],int(800-int(countList[i][1])),(int(countList[i][1]*1.75)),int(countList[i][1])])
    pygame.display.flip()
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()##ends pygame to make it idlefriendly
