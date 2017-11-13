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
colorList=[black,red,green,yellow,purple,lgreen,brown] #list of possible enemy colors
size=[800,600] 
pi=math.pi
screen=pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption("Agrio Clone")
clock=pygame.time.Clock()
playerInfo=[50,50,5,blue] ##x,y,size,color
pvector=[0,0] #x,y
eInfo=[]
eVec=[]
for i in range(0,25): #generates the list of enemys and their directions
    size=random.randint(3,20)
    eInfo.append([random.randint(100,700),random.randint(100,500),size,colorList[random.randint(0,len(colorList)-1)],0])
    eVec.append([int((21-eInfo[i][2])/3),int((21-eInfo[i][2]))/3])
    if int((21-eInfo[i][2]%2)) != 1:
        eVec[i-1][0]=eVec[i][0]*-1
    else:
        eVec[i][1]=eVec[i][0]*-1
    
def playerDraw(player,direc):
    """draws the player and handles their direction"""
    pygame.draw.circle(screen,player[3],[player[0],player[1]],player[2])
    player[0]=player[0]+int(direc[0]/(player[2]/3))
    player[1]=player[1]+int(direc[1]/(player[2]/3))
def enemyDraw(player,direc):
    """draws enemys and handels their directions"""
    pygame.draw.circle(screen,player[3],[player[0],player[1]],player[2])
    player[0]=player[0]+int(direc[0])
    player[1]=player[1]+int(direc[1])
def colliosionCheck(enemy,player):
    """Checks for collisons between the players and the enemies"""
    d=math.sqrt(abs((player[0]-enemy[0])**2+(player[1]-enemy[1])**2))
    r=(enemy[2])+(player[2])
    return d<=r
done=False
pygame.display.flip() #makes sure the display prints
while done==False:
    clock.tick(30)
    screen.fill(white)
    pos=pygame.mouse.get_pos()
    pvector[0]=pos[0]-playerInfo[0] ##updates the players speed and vector
    pvector[1]=pos[1]-playerInfo[1]
    for i in range(0,len(eInfo)): ##draws all the enemys, handles bouncing
        enemyDraw(eInfo[i],eVec[i])
        if eInfo[i][0]>800 or eInfo[i][0]<0:
            eVec[i][0]=-1*eVec[i][0]
        if eInfo[i][1]>600 or eInfo[i][1]<0:
            eVec[i][1]=-1*eVec[i][1]
        if colliosionCheck(eInfo[i],playerInfo)==True: #handles collison
            print("You Hit something!")
            if playerInfo[2]>eInfo[i][2]:
                playerInfo[2]=playerInfo[2]+eInfo[i][2]
                eInfo.pop(i)
                eVec.pop(i)
                break
            else:
                pygame.quit()
                print("you died")
                done=True
                break
    playerDraw(playerInfo,pvector)
    pygame.display.update()
    if eInfo==[]:
        pygame.quit()
        done=True
        print("Congragulations, you won!")
        break
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()
