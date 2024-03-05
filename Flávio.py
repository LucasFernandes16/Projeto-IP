# Criando o personagem
class Player(pygame.sprite.Sprite): # Usando herança de Sprite's para facilitar a colisão entre os pixels do jogador com os blocos
    COLOR = (255, 0, 0)

    # Aqui a altura e largura serão determinadas pela imagem q estamos usando para o nosso personagem
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height) # Adicionado todos esses valores em retângulo fica mais fácil de acessar e resolver os problemas das colisões
        self.x_vel = 0
        self.y_vel = 0
        # Pesquisem sobre dps:
        self.mask = None #Armazena a máscara de colisão correspondente à imagem do objeto, que é usada para detecção de colisão mais precisa
        
        self.animation_count = 0 # sem isso vc redefine a animação em quanto o palyer está se movendo e vai bugar a tela

    # Apenas a direção de movimento 
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
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
        self.move(self.x_vel, self.y_vel)

    # Desenha o player na tela
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)