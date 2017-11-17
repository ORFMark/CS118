import pygame
pygame.init()
black = [0,0,0]
blue = [0,0,255]
red = [255,0,0]

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
    print(player_dirx)
    print(player_diry)
while done == False:
    clock.tick(60)
    #drawing happens here -----------

    screen.fill(blue)

    font = pygame.font.Font(None, 25)

    text = font.render("Agar", True, black)

    screen.blit(text, [400,20])

    draw_player(player_x,player_y,player_radius)

    update_player_position()

    pos = list(pygame.mouse.get_pos())
    update_player_direction(pos)
    pygame.mouse.set_visible(False)

    pygame.display.flip()    
    #drawing ends ---------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
