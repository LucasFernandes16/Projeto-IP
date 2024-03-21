import os
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
def init_tela():
    background = pygame.image.load(join("assets", "Screens",'Home.png'))
    window.blit(background, (0,0))
    pygame.display.update()
