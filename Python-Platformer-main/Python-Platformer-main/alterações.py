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

# Criando o personagem
class Player(pygame.sprite.Sprite): # Usando herança de Sprite's para facilitar a colisão entre os pixels do jogador com os blocos
    
    # Aqui a altura e largura serão determinadas pela imagem q estamos usando para o nosso personagem
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height) # Adicionado todos esses valores em retângulo fica mais fácil de acessar e resolver os problemas das colisões
        self.x_vel = 0
        self.y_vel = 0
        # Pesquisem sobre dps:
        self.mask = None #Armazena a máscara de colisão correspondente à imagem do objeto, que é usada para detecção de colisão mais precisa
        
        self.animation_count = 0 # sem isso vc redefine a animação em quanto o palyer está se movendo e vai bugar a tela

    # Apenas a direção de movimento 
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        self.x_vel = -vel # a velocidade é negativa, pq se vc quiser ir para trás estará removendo os quadros relativo a tela do jogo, recomendo verem essa parte do vídeo e uma representação dos eixos no pygame
    
    # O resto é entendível aq
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0


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
def draw(window, background, bg_image):
    # Percorrendo cada bloco para poder desenhar sobre ele
    for tile in background:
        # window.blit é usado para atualizar o conteúdo da janela do jogo a cada quadro
        window.blit(bg_image, tile)

    pygame.display.update() # Atualizando a tela a cada frame

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png") # bg_image é a imagem de fundo 

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background, bg_image) #chamando a def do fundo 
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
