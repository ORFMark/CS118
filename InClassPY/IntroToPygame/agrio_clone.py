import pygame
import random
import math
pygame.init()
black=[0,0,0] ##colors
red=[255,0,0]
green=[0,255,0]
blue=[0,0,255]
white=[255,255,255]
yellow=[255,255,0]
purple=[255,0,255]
lgreen=[102,209,114]
brown=[104,94,49]
colorList=[black,red,green,yellow,purple,lgreen,brown]
size=[600,400]
pi=math.pi
screen=pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.set_caption("Agrio Clone")
clock=pygame.time.Clock()
playerInfo=[200,300,20,blue] ##x,y,size,color
pvector=[0,0] #x,y
eInfo=[]
eVec=[]
for i in range(0,10):
    eInfo.append([random.randint(100,500),random.randint(100,300),random.randint(3,10),colorList[random.randint(0,len(colorList)-1)],0])
    eVec.append([random.randint(-5,5),random.randint(-15,15)])
def playerDraw(player,direc):
    pygame.draw.circle(screen,player[3],[player[0],player[1]],player[2])
    player[0]=player[0]+int(direc[0]/player[2])
    player[1]=player[1]+int(direc[1]/player[2])
done=False
while done==False:
    clock.tick(30)
    screen.fill(white)
    pos=pygame.mouse.get_pos()
    pvector[0]=pos[0]-playerInfo[0]
    pvector[1]=pos[1]-playerInfo[1]
    for i in range(0,len(eInfo)):
        playerDraw(eInfo[i],eVec[i])
        if eInfo[i][0]>600 or eInfo[i][0]<0:
            eVec[i][0]=-1*eVec[i][0]
        if eInfo[i][1]>400 or eInfo[i][1]<0:
            eVec[i][1]=-1*eVec[i][1]
        if eInfo[i][0]-(playerInfo[0]-playerInfo[2])<eInfo[i][2] and eInfo[i][0]-(playerInfo[0]+playerInfo[2])<eInfo[i][2] and eInfo[i][1]-(playerInfo[1]-playerInfo[2])<eInfo[i][2] and eInfo[i][1]-(playerInfo[1]+playerInfo[2])<eInfo[i][2]:
            playerInfo[2]=playerInfo[2]+eInfo[i][2]
            eInfo.pop(i)
            break
    playerDraw(playerInfo,pvector)
    pygame.display.flip()
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()
