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

# sprite da aparição
class Appering(self):
    
    ANIMATION_DELAY = 3
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "appering") # passando o nome 'fire' para o objeto
        self.appering = load_sprite_sheets("assets", "Items", 'Effect', 96, 96) #carregando as sprites das armadilhas de disparo automátioo 
        self.image = self.appering["Appering"][0] #inicializando a imagem do fogo apagado'off'
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0 
        self.animation_name = "on" 


    def loop(self):
        sprites = self.appering[self.animation_name]# utilizando self.fire para obter as animações de fogo aceso e apagado
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index] #define o sprite atual do fogo
        self.animation_count += 1 #acrescenta o contador da animação do fogo

        if self.animation_count == 5:
            break
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
