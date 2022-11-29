import pygame

class Caracter:
    def __init__(self,x,y,address,vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.address = address
    def move(self,win):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        elif keys[pygame.K_RIGHT]:
            self.x += self.vel
        elif keys[pygame.K_UP]:
            self.y -= self.vel
        elif keys[pygame.K_DOWN]:
            self.y += self.vel
        pygame.draw.rect(win, (255, 0, 0,), (self.x,self.y,40,40))

class Wall:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def create(self,win):
        pygame.draw.rect(win, (255, 0, 0,), (self.x,self.y,50,50))
        