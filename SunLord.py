import pygame

def flip(sprites):
    # Função que inverte as imagens horizontalmente
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    # Função para carregar spritesheets e criar sprites a partir delas
    path = join("assents", dir1, dir2)
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

ANIMATION_DELAY = 3  # Define o atraso entre as animações

def update_sprite(self):
    # Função para atualizar o sprite com base no estado do personagem
    sprite_sheet = "idle"
    if self.x_vel != 0:
        sprite_sheet = "run"  # Se o personagem estiver se movendo, muda para os sprites "run" 

    sprite_sheet_name = sprite_sheet + "_" + self.direction  # Concatenação para obter o nome correto da sprite sheet
    sprites = self.SPRITES[sprite_sheet_name]  # Obtém os sprites correspondentes à sprite sheet atual
    sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)  # Calcula o índice do sprite a ser exibido com base no atraso entre as animações
    self.sprite = sprites[sprite_index]  # Define o sprite atual
    self.animation_count += 1  # Incrementa o contador de animação
    self.update()  # Chama a função de atualização

def update():
    self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))  # Atualiza a posição do retângulo do sprite
    self.mask = pygame.mask.from_surface(self.sprite)  # Atualiza a colisão do sprite