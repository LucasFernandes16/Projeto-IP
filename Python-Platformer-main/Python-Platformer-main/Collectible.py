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


path = pygame.image.load("assets/MainCharacters/NinjaFrog")