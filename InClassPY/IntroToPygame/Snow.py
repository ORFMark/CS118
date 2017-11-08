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
green=[102,209,114]
brown=[104,94,49]
pi=math.pi
size=[800,800]
pos_list=[]
vectorList=[]
sizeList=[]
countList=[]
count=0
def drawHouse():
    pygame.draw.rect(screen,green,[300,650,200,150])
    pygame.draw.rect(screen,black,[450,580,20,40])
    pygame.draw.polygon(screen,brown,[[270,650],[400,575],[530,650]])
    pygame.draw.rect(screen,brown,[425,720,50,80])
    pygame.draw.rect(screen,yellow,[325,710,60,40])
    pygame.draw.rect(screen,brown,[325,710,60,40],3)
for i in range (0,300):
    x=random.randint(1,800)
    y=random.randint(0,700)
    #y=random.randint(-20,0)
    pos_list.append([x,y])
    countList.append([x,0])
screen=pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.set_caption("Happy Holidays")
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
        pygame.draw.ellipse(screen,white,[countList[i][0]-20,int(800-int(countList[i][1])),(int(countList[i][1]*1.75)),int(countList[i][1])])
        drawHouse()
        pygame.draw.line(screen,white,[270,650],[400,575],int(count))
        pygame.draw.line(screen,white,[400,575],[530,650],int(count))
        if count>=15:
            
    pygame.display.flip()
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()##ends pygame to make it idlefriendly
