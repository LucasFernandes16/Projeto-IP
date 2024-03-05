import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

pygame.display.set_caption("Dnamel Adventure")

tela = pygame.display.set_mode((largura, altura))

while True:
    for event in pygame.event.get():
        if event == quit:
            pygame.quit()
            exit()
    pygame.display.update()
