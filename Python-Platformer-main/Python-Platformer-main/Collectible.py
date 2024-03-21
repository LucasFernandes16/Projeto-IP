import pygame
from  Sprites import load_sprite_sheets

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

class Collectible(Object):
    ANIMATION_DELAY = 3
    
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height, name)
        self.collectible = load_sprite_sheets("Items", "Fruits", width, height)
        self.image = self.collectible[name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = name
        self.hit = False

    def hit_collectible(self):
        self.hit = True
        
    def loop(self):
        if self.hit:
            self.animation_name = "Collected"
        
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

# fruit = (230, HEIGHT - block_size - 64 , 32, 32, "Melon")
