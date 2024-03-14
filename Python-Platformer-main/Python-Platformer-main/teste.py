import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Dnamel Adventure")

WIDTH, HEIGHT = 900, 700
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

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

def update_sprite(self):
    # Função para atualizar o sprite com base no estado do personagem
    sprite_sheet = "idle"
    if self.x_vel != 0:
        sprite_sheet = "run"  # Se o personagem estiver se movendo, muda para os sprites "run" 

    sprite_sheet_name = sprite_sheet + "" + self.direction  # Concatenação para obter o nome correto da sprite sheet
    sprites = self.SPRITES[sprite_sheet_name]  # Obtém os sprites correspondentes à sprite sheet atual
    sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)  # Calcula o índice do sprite a ser exibido com base no atraso entre as animações
    self.sprite = sprites[sprite_index]  # Define o sprite atual
    self.animation_count += 1  # Incrementa o contador de animação
    self.update()  # Chama a função de atualização

def update():
    self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))  # Atualiza a posição do retângulo do sprite
    self.mask = pygame.mask.from_surface(self.sprite)  # Atualiza a colisão do sprite

# Criando o personagem
class Player(pygame.sprite.Sprite): # Usando herança de Sprite's para facilitar a colisão entre os pixels do jogador com os blocos
    COLOR = (255, 0, 0)
    GRAVITY = 1########
    SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    ANIMATION_DELAY = 3

    # Aqui a altura e largura serão determinadas pela imagem q estamos usando para o nosso personagem
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height) # Adicionado todos esses valores em retângulo fica mais fácil de acessar e resolver os problemas das colisões
        self.x_vel = 0
        self.y_vel = 0
        # Pesquisem sobre dps:
        self.mask = None #Armazena a máscara de colisão correspondente à imagem do objeto, que é usada para detecção de colisão mais precisa
        self.direction = "right"
        self.animation_count = 0 # sem isso vc redefine a animação em quanto o palyer está se movendo e vai bugar a tela
        self.fall_count = 0#######
        self.jump_count = 0

    # Apenas a direção de movimento 
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def jump(self):
        self.y_vel = -self.GRAVITY * 7 #a gravidade vai negativa para que ele pule no ar, ou seja fique mais "leve" e vá para cima
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0 #isso faz com que quando eu pule consiga me livrar da gravidade 
    
    def move_left(self, vel):
        self.x_vel = -vel # a velocidade é negativa, pq se vc quiser ir para trás estará removendo os quadros relativo a tela do jogo, recomendo verem essa parte do vídeo e uma representação dos eixos no pygame
    # O resto é entendível aq
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    # Uma def com relação ao loop while e garente a movimentação e atualização do player na tela
    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)#sempre empurrando para baixo constantemente 
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1############

    def update_sprite(self):
    # Função para atualizar o sprite com base no estado do personagem
        sprite_sheet = "idle"
        if self.x_vel != 0:
            sprite_sheet = "run"  # Se o personagem estiver se movendo, muda para os sprites "run" 

        sprite_sheet_name = sprite_sheet + "" + self.direction  # Concatenação para obter o nome correto da sprite sheet
        sprites = self.SPRITES[sprite_sheet_name]  # Obtém os sprites correspondentes à sprite sheet atual
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)  # Calcula o índice do sprite a ser exibido com base no atraso entre as animações
        self.sprite = sprites[sprite_index]  # Define o sprite atual
        self.animation_count += 1  # Incrementa o contador de animação
        self.update()  # Chama a função de atualização

    def update():
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))  # Atualiza a posição do retângulo do sprite
        self.mask = pygame.mask.from_surface(self.sprite)  # Atualiza a colisão do sprite

    # Desenha o player na tela
    def draw(self, win):
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))

# Apenas definindo a classe de objetos para usar herença nos outros objetos q iremos criar no jogo
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        # a única coisa q vamos mudar será a imagem q vai ser desenhada, de resto teremos as propiedades po padrão sem precisar reescrever 
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

# Criando os blocos
class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size) # Repetimos size pq oq queremos é um quadrado
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)#criando a máscara de colisão para ser ocultado da superfíce


# Criando o fundo do jogo
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name)) # Acessando a pasta que contém a imagem que usaremos de fundo
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):  # Dividindo o fundo por cada azulejo no eixo x
        for j in range(HEIGHT // height + 1): # O mesmo para o eixo y
            pos = (i * width, j * height)
            tiles.append(pos)

    # Retorna imagem para sabermos qual foi usada
    return tiles, image 

# Desenhando o fundo
def draw(window, background, bg_image, player, floor):
    # Percorrendo cada bloco para poder desenhar sobre ele
    for tile in background:
        # window.blit é usado para atualizar o conteúdo da janela do jogo a cada quadro
        window.blit(bg_image, tile)
    
    for obj in floor:
        obj.draw(window)
    
    player.draw(window)

    pygame.display.update() # Atualizando a tela a cada frame


#função responsável por mover nosso personagem principal na tela 
def handle_move(player, objects):
    keys = pygame.key.get_pressed() #informa todas as teclas que estão sendo pressionadas no comento 
    player.x_vel = 0 
    #criando a responsividade para apertar a tecla e mover o personagem
    if keys[pygame.K_LEFT]: 
        player.move_left(PLAYER_VEL) # passando o quanto o player vai se mover 
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png") # bg_image é a imagem de fundo 
    block_size = 96

    player = Player(100, 100, 50, 50) # Os parâmetros para cosntruir o player na tela 
    #faltaa comentar
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
            for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN: #checando se tem uma tecla pressionada 
                if event.key == pygame.K_SPACE and player.jump_count < 2: #se a tecla for espaço e o contador dos nossos pulos for menor que dois, vai poder pular duas vezes
                    player.jump()
        player.loop(FPS)
        handle_move(player, floor)

        draw(window, background, bg_image, player, floor) #chamando a def do fundo 

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
