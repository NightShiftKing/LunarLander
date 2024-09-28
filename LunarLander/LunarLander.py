import pygame
from Lander import Lander
pygame.init()

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

screen = pygame.display.set_mode((700,1000))
pygame.display.set_caption('Lunar Lander Simulator')

gameover = False
clock = pygame.time.Clock()

Lander = Lander(350,0,0,0,0,0,False,False,False) 

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical Velocity:', False, (0, 200, 200))
text2 = font.render(str(int(Lander.yVel)), 1, (0, 200, 200))
text3 = font.render('YOU CRASHED:', False, (200, 50, 50))
text4 = font.render('Vertical Velocity:', False, (200, 20, 20))
text5 = font.render(str(int(Lander.yVel)), 1, (200, 20, 20))
text6 = font.render('Height:', False, (0, 200, 200))
text7 = font.render(str(int(Lander.ypos)), 1, (20, 200, 200))


while not gameover:
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True


   


    #keyboard input-----------------------------------

    Lander.Move_Lander()





    text2 = font.render(str("%.2f" %(Lander.yVel*-1)), 1, (0,200,200))
    text5 = font.render(str("%.2f" %(Lander.yVel*-1)), 1, (200,20,20))

    text6 = font.render('Height:', False, (0, 200, 200))
    text7 = font.render(str(int(1000-Lander.ypos)), 1, (20, 200, 200))
     
    #render section-----------------------------------vis
    screen.fill((0,0,0))

    Lander.draw_Lander(screen)

    if abs(Lander.yVel) < .5:
        screen.blit(text1, (10,10))
        screen.blit(text2,(250,10))
    else:
        screen.blit(text4,(10,10))
        screen.blit(text5,(250,10))

    if Lander.onGround == True and abs(Lander.yVel) >.5:
        Lander.crash = True
        screen.blit(text3,(200,500))
        pygame.display.flip
        pygame.time.wait(1000)
        Lander.xpos = 350
        Lander.ypos = 0
        Lander.xVel = 0
        Lander.yVel = 0
        Lander.onGround = False 

    screen.blit(text6, (10,60))
    screen.blit(text7,(150,60))

    pygame.draw.rect(screen, (128,128,128), (0, 800, 700, 1000)) 


    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()