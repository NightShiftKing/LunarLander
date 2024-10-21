import random
import pygame
pygame.init()

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

screen = pygame.display.set_mode((700,1000))
pygame.display.set_caption('Lunar Lander Simulator')

gameover = False
clock = pygame.time.Clock()

playerX = 350 
playerY = 0
playerXVel = 0
playerYVel = -10/60
onGround, rocketOn, crashed, = False, False, False 

def star():

    for i in range(100):
        xpos = random.randrange(700)
        ypos = random.randrange(800)    
        pygame.draw.circle(screen, (255,255,255), (xpos, ypos), 2) 


pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical velocity:', False, (0,200,200))
text2 = font.render(str(int(playerYVel)), 1, (0,200,200))
text3 = font.render('YOU CRASHED:', False, (200,50,50))
text4 = font.render('Vertical velocity:', False, (200,20,20))
text5 = font.render(str(int(playerYVel)), 1, (200,20,20))
text6 = font.render('Height', False, (20,20,200))
text7 = font.render(str(int(playerY)), 1, (20,20,200))

while not gameover:
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True


   


    #keyboard input-----------------------------------
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        playerYVel -= 0.417/60
        onGround = False 
        rocketOn = True
    else:
        rocketOn = False
        if not onGround:
            playerYVel +=  0.165/60
    

    if key[pygame.K_a]:
        playerXVel -= 1/60
    elif key[pygame.K_d]:
        playerXVel += 1/60

    if playerY >= 800:
        onGround = True





    if onGround and abs(playerYVel)>.5:
        crashed = True
        screen.blit(text3, (200,500))
        pygame.display.flip()
        pygame.time.wait(1000)
        playerX = 350
        playerY = 0
        playerXVel = 0
        playerYVel = 0
        onGround = False

    if onGround and abs(playerYVel)<=.5:
        pygame.time.wait(1000)
        playerX = 350
        playerY = 0
        playerXVel = 0
        playerYVel = 0
        onGround = False        

    playerX += playerXVel
    playerY += playerYVel

    text2 = font.render(str("%.2f" %(playerYVel*-1)), 1, (0,200,200))
    text5 = font.render(str("%.2f" %(playerYVel*-1)), 1, (200,20,20))

    text6 = font.render('Height', False, (20,20,200))
    text7 = font.render(str(int(800-playerY)), 1, (20,20,200))
    #render section-----------------------------------vis
    screen.fill((0,0,0))

    pygame.draw.circle(screen,(0,255,255), (playerX,playerY), 20)
    pygame.draw.rect(screen, (128,128,128), (0, 800, 700, 1000))

    if abs(playerYVel)< 0.5:
        screen.blit(text1,(10,10))
        screen.blit(text2, (250,10))
    else:
        screen.blit(text4, (10,10))
        screen.blit(text5, (250,10))
    screen.blit(text6, (10,60))
    screen.blit(text7, (150,60))



    star()


    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()