import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
def iniciar_tela():
    fundo=pygame.image.load('inicial.png')
    window.blit(fundo, (0,0))
    pygame.display.update()
