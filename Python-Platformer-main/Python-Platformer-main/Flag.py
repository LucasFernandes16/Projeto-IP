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


class Flag(Object):
    ANIMATION_DELAY = 4

    def __init__(self, x, y, width, height,):
        super().__init__(x, y, width, height, "flag")
        self.flag = load_sprite_sheets("Items", "Checkpoints", width, height)
        self.image = self.flag["Checkpoint (No Flag)"][0]
        self.animation_count = 0
        self.animation_name = "Checkpoint (Flag Idle)(64x64)"
        self.hit = False

    def hit_flag(self):
        self.hit = True

    def flag_idle(self):
        self.animation_name = "Checkpoint (Flag Idle)(64x64)"
        

    def loop(self): 
        if self.hit:
            self.image = self.flag["Checkpoint (Flag Out) (64x64)"][0]
        elif self.animation_count == 25:
            self.animation_name = "Checkpoint (Flag Idle)(64x64)"
        
        sprites = self.flag[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0