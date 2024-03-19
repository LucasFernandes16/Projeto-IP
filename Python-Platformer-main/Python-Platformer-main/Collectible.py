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
            self.image = self.collectible["Collected"][0]
        
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

fruit = (230, HEIGHT - block_size - 64 , 32, 32, "Melon")


def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run" # Se o personagem estiver se movendo, muda para os sprites "run" 

        sprite_sheet_name = sprite_sheet + "_" + self.direction # Concatenação para obter o nome correto da sprite sheet
        sprites = self.SPRITES[sprite_sheet_name] # Obtém os sprites correspondentes à sprite sheet atual
        
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites) # Calcula o índice do sprite a ser exibido com base no atraso entre as animações
        
        self.sprite = sprites[sprite_index]  # Define o sprite atual
        self.animation_count += 1 # Incrementa o contador de animação
        self.update() # Chama a função de atualização



