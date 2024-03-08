import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Dnamel Adventure")

WIDTH, HEIGHT = 680, 480
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

# Criando o fundo do jogo
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name)) # Acessando a pasta que contém a imagem que usaremos de fundo
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):  # Dividindo o fundo por cada azulejo no eixo x
        for j in range(HEIGHT // height + 1): # O mesmo para o eixo y
            pos = (i * width, j * height)
            tiles.append(pos)

    # Retorna imagem para sabermos qual foi usada
    return tiles, image 

# Desenhando o fundo
def draw(window, background, bg_image, player):
    # Percorrendo cada bloco para poder desenhar sobre ele
    for tile in background:
        # window.blit é usado para atualizar o conteúdo da janela do jogo a cada quadro
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update() # Atualizando a tela a cada frame

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png") # bg_image é a imagem de fundo 

    player = Player(100, 100, 50, 50) # Os parâmetros para cosntruir o player na tela 

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player) #chamando a def do fundo 
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
