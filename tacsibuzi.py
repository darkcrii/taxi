import pygame
import socket

#importing classes
from classes import *

pygame.init()

game = pygame.display.set_mode((1100,1100))


def create_map():
    map = [17][17]
    for i in range(17):
        for j in range(17):


run_game = True

caracter1 = Caracter(10,10,10,10)

while run_game:
    pygame.time.delay(100)
    caracter1.move(game)
    pygame.display.update()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run_game = False
    
    game.fill((0,0,0))



pygame.quit()

