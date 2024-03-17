def flip(sprites):
    # Função que inverte as imagens horizontalmente
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    # dir1 é a pasta onde as sprites estão guardadas 
    # dir2 é a sprite q vc quer usar
    
    # Função para carregar spritesheets e criar sprites a partir delas
    path = join("assets", dir1, dir2)
    # Lista todos os arquivos no diretório, filtrando apenas os arquivos que são arquivos de fato

    images = [f for f in listdir(path) if isfile(join(path, f))] 

    all_sprites = {} # Dicionário para armazenar todos os sprites carregados

    # Itera sobre cada imagem encontrada no diretório
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha() # Carrega a sprite sheet como uma superfície

        sprites = [] # Lista para armazenar os sprites individuais da sprite sheet
        
        for i in range(sprite_sheet.get_width() // width):  # Loop para percorrer horizontalmente a sprite sheet
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32) # Cria uma superfície para cada sprite individual
           
            # Define a região do sprite na sprite sheet
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect) # Copia o sprite da sprite sheet para a superfície
            # Escala o sprite para o dobro do tamanho
            sprites.append(pygame.transform.scale2x(surface)) 
        
        # Verifica se a direção está ativada
        if direction:
            # Adiciona os sprites invertidos para a direita e para a esquerda
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites) # Chama a função flip para inverter os sprites
        # Adiciona os sprites sem alteração ao dicionário
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites