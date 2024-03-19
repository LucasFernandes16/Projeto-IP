import os
import pygame
from os import listdir
from os.path import isfile, join

FPS = 60
WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Criando o fundo do jogo
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name)) # Acessando a pasta que contém a imagem que usaremos de fundo
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1): # Dividindo o fundo por cada azulejo no eixo x
        for j in range(HEIGHT // height + 1): # O mesmo para o eixo y
            pos = (i * width, j * height)
            tiles.append(pos)
    
    # Retorna imagem para sabermos qual foi usada
    return tiles, image

# Desenhando o fundo
def draw(window, background, bg_image, player, objects, offset_x, coletavel):
    # Percorrendo cada bloco para poder desenhar sobre ele
    for tile in background:
        # window.blit é usado para atualizar o conteúdo da janela do jogo a cada quadro
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)
    
    for colect in coletavel:
        colect.draw(window, offset_x)
    
    player.draw(window, offset_x)

    if player.alive == False:# preenchendo a tela com preto quando o boneco tiver vida menor que 0
        window.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game Over', True, (255,192,203))
        textRect = text.get_rect()
        textRect.center = (HEIGHT // 1.6 , HEIGHT // 2)
        window.blit(text, textRect)#escrevendo na tela a mensagem Game Over

    pygame.display.update() # Atualizando a tela a cada frame