# Importa os módulos necessários para o funcionamento do jogo
import pygame
import sys

# Define as dimensões da tela e a taxa de quadros por segundo (FPS)
SCREENWIDTH, SCREENHEIGHT = 1280, 720
FPS = 60

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Define a classe principal do jogo, responsável por inicializar e controlar o jogo
class Game:
    def __init__(self):
        # Inicializa o pygame
        pygame.init()
        # Cria a tela do jogo com base nas dimensões definidas
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        # Cria um relógio para controlar a taxa de atualização do jogo
        self.clock = pygame.time.Clock()
        
        # Inicializa o gerenciador de estados do jogo com o estado inicial 'start'
        self.gameStateManager = GameStateManager('start')
        # Cria instâncias das classes Start e Level, passando a tela e o gerenciador de estados como parâmetros
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)

        # Cria um dicionário para mapear os estados do jogo às instâncias correspondentes
        self.states = {'start': self.start, 'level': self.level}
        
        # Cria uma instância do personagem
        self.player = Player()

        # Cria instâncias dos blocos para mudança de tela
        self.block_blue = Block(SCREENWIDTH - 100, SCREENHEIGHT // 2, BLACK)
        self.block_red = Block(50, SCREENHEIGHT // 2, BLACK)

    # Método responsável por executar o jogo
    def run(self):
        # Loop principal do jogo
        while True:
            # Captura os eventos do pygame
            for event in pygame.event.get():
                # Verifica se o evento é de fechamento da janela
                if event.type == pygame.QUIT:
                    # Encerra o pygame e o programa
                    pygame.quit()
                    sys.exit()
            
            # Atualiza a posição do jogador
            self.player.update()

            # Verifica colisão entre o jogador e os blocos de mudança de tela
            if self.gameStateManager.get_state() == 'start':
                if pygame.sprite.collide_rect(self.player, self.block_red):
                    self.gameStateManager.set_state('level')
            elif self.gameStateManager.get_state() == 'level':
                if pygame.sprite.collide_rect(self.player, self.block_blue):
                    self.gameStateManager.set_state('start')

            # Obtém o estado atual do jogo e executa o método run() do estado correspondente
            self.states[self.gameStateManager.get_state()].run()
            
            # Desenha o jogador na tela
            self.player.draw(self.screen)

            # Desenha o bloco de mudança de tela correspondente ao estado atual
            if self.gameStateManager.get_state() == 'start':
                self.block_red.draw(self.screen)
            elif self.gameStateManager.get_state() == 'level':
                self.block_blue.draw(self.screen)

            # Atualiza a tela do jogo
            pygame.display.update()
            # Controla a taxa de quadros por segundo
            self.clock.tick(FPS)

# Define a classe Level, responsável por controlar o estado do jogo no nível
class Level:
    def __init__(self, display, gameStateManager):
        # Inicializa as variáveis display (tela) e gameStateManager (gerenciador de estados)
        self.display = display
        self.gameStateManager = gameStateManager
    
    # Método responsável por executar o estado do jogo no nível
    def run(self):
        # Preenche a tela com a cor azul (RGB: 0, 0, 255)
        self.display.fill(BLUE)  # blue

# Define a classe Start, responsável por controlar o estado do jogo no início
class Start:
    def __init__(self, display, gameStateManager):
        # Inicializa as variáveis display (tela) e gameStateManager (gerenciador de estados)
        self.display = display
        self.gameStateManager = gameStateManager
    
    # Método responsável por executar o estado do jogo no início
    def run(self):
        # Preenche a tela com a cor vermelha (RGB: 255, 0, 0)
        self.display.fill(RED)  # red

# Define a classe GameStateManager, responsável por gerenciar os estados do jogo
class GameStateManager:
    def __init__(self, currentState):
        # Inicializa o estado atual do jogo
        self.currentState = currentState
    
    # Método para obter o estado atual do jogo
    def get_state(self):
        return self.currentState
    
    # Método para definir o estado do jogo
    def set_state(self, state):
        self.currentState = state

# Define a classe Player para representar o personagem do jogo
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Carrega a imagem do jogador
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)  # verde
        self.rect = self.image.get_rect()
        # Define a posição inicial do jogador
        self.rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)
        # Define a velocidade de movimento do jogador
        self.vel = 5

    def update(self):
        # Obtém o estado das teclas pressionadas
        keys = pygame.key.get_pressed()
        # Move o jogador com base nas teclas pressionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        if keys[pygame.K_UP]:
            self.rect.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.rect.y += self.vel

    def draw(self, screen):
        # Desenha o jogador na tela
        screen.blit(self.image, self.rect)

# Define a classe Block para representar os blocos de mudança de tela
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        # Carrega a imagem do bloco
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)  # cor
        self.rect = self.image.get_rect()
        # Define a posição inicial do bloco
        self.rect.center = (x, y)

    def draw(self, screen):
        # Desenha o bloco na tela
        screen.blit(self.image, self.rect)

# Verifica se o código está sendo executado como script principal
if __name__ == '__main__':
    # Cria uma instância do jogo e inicia a execução
    game = Game()
    game.run()