import pygame
from Sprites import load_sprite_sheets

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

#adicionando o fogo animado
class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire") # passando o nome 'fire' para o objeto
        self.fire = load_sprite_sheets("Traps", "Fire", width, height) #carregando as sprites das armadilhas de disparo automátioo 
        self.image = self.fire["off"][0] #inicializando a imagem do fogo apagado'off'
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0 
        self.animation_name = "off" 

    #definindo a classe autodidata que puxa a animaçao do fogo aceso das sprites
    def on(self):
        self.animation_name = "on"
    #animaçao do fogo apagado
    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]# utilizando self.fire para obter as animações de fogo aceso e apagado
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index] #define o sprite atual do fogo
        self.animation_count += 1 #acrescenta o contador da animação do fogo

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image) #mascara de colisao para o fogo

        #evitando que a contagem de animações não fique muito grande já que o fogo é estatico
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0 #se for além da animação volta para a contagem = 0
