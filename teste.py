import pygame
import os
import random
import math
from os import listdir
from os.path import isfile, join
from pygame.locals import *
from sys import exit
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
FPS = 60

pygame.init()

largura = 640
altura = 480

pygame.display.set_caption("Dnamel Adventure")

tela = pygame.display.set_mode((largura, altura))
def telona(tela):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()
    
