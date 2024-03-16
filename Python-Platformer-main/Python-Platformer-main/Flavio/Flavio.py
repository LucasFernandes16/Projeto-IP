import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png") # Acessa a pasta q contém a imagem do bloco
    image = pygame.image.load(path).convert_alpha()

    # Criando a imagem com tamanho do bloco q nós queremos usar
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)

    # Para carregar a imagem desejada iniciamos a contar de 96 pixels de distância do eixo x e teremos o bloco verde
    rect = pygame.Rect(96, 0, size, size) 
    # Isso significa q cada bloco quadrado vísivel possui 8 pixels, 96/8 = 12 quadrados de distância em x

    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def flip(sprites):
    # Função que inverte as imagens horizontalmente
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    # dir1 é a pasta onde as sprites estão guardadas 
    # dir2 é a sprite q vc quer usar
    
    # Função para carregar spritesheets e criar sprites a partir delas
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}  # Dicionário para armazenar todos os sprites

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            # Se houver direção, cria sprites para direita e esquerda
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)  # Chama a função flip para inverter os sprites
        else:
            all_sprites[image.replace(".png", "")] = sprites  # Adiciona os sprites sem direção especificada ao dicionário

    return all_sprites  # Retorna o dicionário contendo todos os sprites


class Collectible(Object):
    ANIMATION_DELAY = 3
    
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height, name)
        self.collectible = load_sprite_sheets("Items", "Fruits", name + ".png", 32, 32, False)
        self.image = self.collectible[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "fruit"
        
    def loop(self):
        sprites = self.collectible[self.animation_name] # Obtém os sprites correspondentes à sprite sheet atual
        
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites) # Calcula o índice do sprite a ser exibido com base no atraso entre as animações
        
        self.sprite = sprites[sprite_index]  # Define o sprite atual
        self.animation_count += 1 # Incrementa o contador de animação
        self.update() # Chama a função de atualização
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y)) # Atualiza a posição do retângulo do sprite
        self.mask = pygame.mask.from_surface(self.sprite) # Atualiza a colisão do sprite
        
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0




class Flag(Object):
    ANIMATION_DELAY = 4

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "flag")
        self.flag = load_sprite_sheets("Items", "Checkpoints", width, height)
        self.image = self.flag["Checkpoint (No Flag)"][0]
        self.animation_count = 0
        self.animation_name = "Checkpoint (No Flag)"

    def hit_flag(self):
        self.animation_name = "Checkpoint (Flag Out) (64x64)"

    def no_flag(self):
        self.animation_name = "Checkpoint (No Flag)"

    def loop(self):
        sprites = self.flag[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

