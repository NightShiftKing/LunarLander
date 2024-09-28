import pygame

class Lander():
    def __init__(self, xpos, ypos, xVel, yVel, xAccel, yAccel, onGround, rocketOn, crash):
        self.xpos = xpos
        self.ypos = ypos
        self.xVel = xVel
        self.yVel = yVel
        self.xAccel = xAccel
        self.yAccel = yAccel
        self.onGround = onGround
        self.rocketOn = rocketOn
        self.crash = crash

    def Move_Lander(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.xAccel = -0.156/60
        elif keys[pygame.K_d]:
            self.xAccel = 0.156/60
        else:
            self.xAccel = 0

        if keys[pygame.K_w]:
            self.yAccel = -0.166/60
            self.onGround = False
            self.rocketOn = True
        else:
            self.rocketOn = False 
            if not self.onGround:
                self.yAccel = 0.156/60

        if self.ypos >= 780:
            self.onGround = True
            self.ypos = 780 

        
        self.xVel += self.xAccel
        self.yVel += self.yAccel

        self.xpos += self.xVel
        self.ypos += self.yVel 

        







    def draw_Lander(self, screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 20, 20))
        