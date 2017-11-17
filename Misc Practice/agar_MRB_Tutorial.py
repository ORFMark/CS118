##This file contains examples and commented explanations of how to draw and collison check enemies per the Agrio assignment. It is meant purely as an educational example resoruce and it will be
##Very obvious if you just copy paste the code. I have tried to make the comments explanatory, and hopefully if you are having trouble this will help you on your way. This is based on the agar.py
##file Ashish sent out and as such I have not added comments to his code (The stuff that controls the player), as he has gone over this in great detail in class. -MRB,11-17-2017
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
colorList=[black,white,green,yellow,purple,lgreen,brown] 
##The above list is a list of a bunch of possible colors, minus red, which is
##the color of the player. We will use this list to randomly assign our enemies colors
pi =3.141592653
size =[800,600]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Agar clone")

done = False
clock = pygame.time.Clock()

player_x = 400
player_y = 300
player_dirx = 0
player_diry = 0
player_radius = 10
enemies=21 ##We are putting enemies in a variable so that we can easily adjust
            ##how many we want to generate

eInfo=[] #Initializes an empty list that we will use to draw and handle our
        #enemies
for i in range(0,enemies):
    x=random.randint(100,700) #Random int for X and Y that leaves a buffer
    y=random.randint(100,500) #around the screen for our player to spawn in
    
    size=random.randint(3,20) #Initalizes random sizes for our enemies
    
    color=colorList[random.randint(0,len(colorList)-1)] #selects a random color
    
    xVec=int((24-size)/4) #Sets up our vectors to be proportoional to size
    yVec=int((24-size)/4)
    
    if i%2==1:       ##These four lines make sure that all our enemies don't end
        xVec=xVec*-1 ##up moving in the same direction by invering the direction
    if i%3==0:       ##on some of them
        yVec=yVec*-1
        
    eInfo.append([[x,y],size,color,[xVec,yVec]]) #generates the list of all the
                 #pos   rad, color   direc       #infomation we need to draw our
                                                 #enemies
def draw_player(x,y,size):                       
    pygame.draw.circle(screen,red,[x,y],size)

def update_player_position():
    global player_x, player_y, player_dirx, player_diry
    player_x += player_dirx
    player_y += player_diry

def update_player_direction(pos):
    global player_dirx, player_diry
    #w = screen.get_width()

    #h = screen.get_height()
    #player_dirx = int (((pos[0] - w/2)/w/2)*20)

    #player_diry = int (((pos[1] - h/2)/h/2)*20)
    player_dirx = pos[0] - player_x
    player_diry = pos[1] - player_y
    
def collison(enemy):
    """Handles collison between the player and the enemy, and returns a bool"""
    d=math.sqrt(abs(((player_x-enemy[0][0])**2)+((player_y-enemy[0][1])**2))) #Distance = sqrt(x2-x1)^2+(y2-y1)^2)
    r=player_radius+enemy[1] #Radius+enemy radius so we are checking the outer core
    return d<=r ##Return the boolean value of that statment

def drawEnemy(enemy):
    """Draws our enemies and handles their direction"""
    if enemy[0][0]>=800 or enemy[0][0]<=0: ##Handles X out of bounds
        enemy[3][0]=enemy[3][0]*-1
    if enemy[0][1]>=600 or enemy[0][1]<=0: ##Handles Y out of bounds
        enemy[3][1]=enemy[3][1]*-1
    enemy[0][0]+=enemy[3][0] ##adds the X and Y vectors to their corrdinates
    enemy[0][1]+=enemy[3][1]
    pygame.draw.circle(screen,enemy[2],enemy[0],enemy[1]) ##Draws the enemies themselves
    
while done == False:
    clock.tick(30)
    #drawing happens here -----------

    screen.fill(blue)

    font = pygame.font.Font(None, 25)

    text = font.render("Agar", True, black)

    screen.blit(text, [400,20])

    draw_player(player_x,player_y,player_radius)

    update_player_position()

    pos = list(pygame.mouse.get_pos())
    update_player_direction(pos)
    for i in range (0,len(eInfo)): ##this loop handles everything to do with our enemies
        enemy=eInfo[i]
        drawEnemy(enemy) ##draws our enemies using the infomation we specified
        if collison(enemy) == True: ##handles what happens if the player and an enemy collide
            if player_radius>=enemy[1]:
                player_radius+=enemy[1]
                eInfo.pop(i) ##removes the dead enemy from the list of enemies
                break ##Prevents out of index range errors
            if player_radius<enemy[1]: ##handles death condition
                done=True
                print("You Died")
                break
    pygame.mouse.set_visible(False)

    pygame.display.flip()    
    #drawing ends ---------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
