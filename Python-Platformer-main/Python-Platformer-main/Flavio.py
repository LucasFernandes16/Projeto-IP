import pygame

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

# Zera os contadores ao colidir com o objeto
def landed(self):
    self.fall_count = 0 
    self.y_vel = 0
    self.jump_count = 0


def hit_head(self):
    self.count = 0
    self.y_vel *= -1 # A velocidade na vertical fica negativa para ele ricochetear em direção ao chão

# Função para determinar a colisão vertical
def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj): # Pela herança da classe sprite.Sprite usamos a "mask" dela para facilitar a nossa colisão
        # Passamos o nosso player e os objetos q iremos colidir

        # Aqui temos os dois tipos de colisão:
            # O player caindo encima do objeto
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
            # dy é deslocamento em y, velocidade em y

        collided_objects.append(obj) 
    return collided_objects # Para sabermos quais objetos estamos colidindo

