import pygame
import os
from os import listdir
from os.path import isfile, join
from Sprites import flip, load_sprite_sheets


# Criando o personagem
class Player(pygame.sprite.Sprite): # Usando herança de Sprite's para facilitar a colisão entre os pixels do jogador com os blocos
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "PinkMan", 32, 32, True)
    ANIMATION_DELAY = 5
    
    # Aqui a altura e largura serão determinadas pela imagem q estamos usando para o nosso personagem
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height) # Adicionado todos esses valores em retângulo fica mais fácil de acessar e resolver os problemas das colisões
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None #Armazena a máscara de colisão correspondente à imagem do objeto, que é usada para detecção de colisão mais precisa
        self.direction = "left"
        self.animation_count = 0 # sem isso vc redefine a animação em quanto o palyer está se movendo e vai bugar a tela
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.health = 3
        self.alive = True # alive definindo se o boneco esta vivo ou morto
        
    def jump(self):
        self.y_vel = -self.GRAVITY * 7 #a gravidade vai negativa para que ele pule no ar, ou seja fique mais "leve" e vá para cima
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0 #isso faz com que quando o player pule consiga se livrar da gravidade 
    
    # Apenas a direção de movimento 
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.x_vel = -vel # a velocidade é negativa, pq se vc quiser ir para trás estará removendo os quadros relativo a tela do jogo, recomendo verem essa parte do vídeo e uma representação dos eixos no pygame
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
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY) #sempre empurrando para baixo constantemente 
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 1:
            self.health -= 1 # decrescendo a quantidade de coração assim que o contador de dano parar
            self.hit = False
            self.hit_count = 0  
        elif self.fall_count > 100:
            self.health -=1
        
        if self.health < 0:
                self.alive = False# mata o boneco quando a vida estiver 0

            
            
        self.fall_count += 1
        self.update_sprite()

    # Zera os contadores ao colidir com o objeto
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1 # A velocidade na vertical fica negativa para ele ricochetear em direção ao chão

    # Função para atualizar o sprite com base no estado do personagem
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

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y)) # Atualiza a posição do retângulo do sprite
        self.mask = pygame.mask.from_surface(self.sprite) # Atualiza a colisão do sprite
    
    def full_hearts(self):# criando a classe full_heart

        path = join("assets", "Items", 'Heart', "full_heart.png")
        full_heart = pygame.image.load(path).convert_alpha()

        for heart in range(self.health):
            window.blit(full_heart,(heart *50,45)) #adicionando os coracoes com base na quantidade de coracao do personagem no canto superior esquerdo
    
    # Desenha o player na tela
    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        
        path = join("assets", "Items", 'Heart', "full_heart.png")#carregando a sprite do coracao
        full_heart = pygame.image.load(path).convert_alpha()

        for heart in range(self.health):
            window.blit(full_heart,(heart *50,45))#adicionando os coracoes com base na quantidade de coracao do personagem no canto superior esquerdo