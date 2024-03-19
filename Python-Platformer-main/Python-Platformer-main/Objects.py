import pygame
import os 
from os import listdir
from os.path import isfile, join
from Traps import Fire

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png") # Acessa a pasta q contém a imagem do bloco
    image = pygame.image.load(path).convert_alpha()

    # Criando a imagem com tamanho do bloco q nós queremos usar
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)

    # Para carregar a imagem desejada iniciamos a contar de 96 pixels de distância do eixo x e teremos o bloco verde
    rect = pygame.Rect(96, 128, size, size) 
    # Isso significa q cada bloco quadrado vísivel possui 8 pixels, 96/8 = 12 quadrados de distância em x

    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

# Apenas definindo a classe de objetos para usar herença nos outros objetos q iremos criar no jogo
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

# Criando os blocos
class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size) # Repetimos size pq oq queremos é um quadrado
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image) #criando a máscara de colisão para ser ocultado da superfíce