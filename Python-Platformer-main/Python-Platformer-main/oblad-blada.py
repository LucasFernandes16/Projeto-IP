import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição de algumas cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definição das dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Classe para criar objetos coletáveis
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(x, y))

# Classe para representar o jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        # Movimento do jogador
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Função principal
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Colisão com Objetos Coletáveis em Pygame")

    clock = pygame.time.Clock()

    # Criando um grupo de sprites para os objetos coletáveis e o jogador
    collectibles_group = pygame.sprite.Group()
    player_group = pygame.sprite.GroupSingle()

    # Criando alguns objetos coletáveis e adicionando ao grupo
    collectible1 = Collectible(200, 200)
    collectible2 = Collectible(400, 300)
    collectibles_group.add(collectible1, collectible2)

    # Criando o jogador
    player = Player()
    player_group.add(player)

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizando a posição do jogador com base nas teclas pressionadas
        keys = pygame.key.get_pressed()
        player.update(keys)

        # Verificando colisões entre o jogador e os objetos coletáveis
        collected_items = pygame.sprite.spritecollide(player, collectibles_group, True)
        for item in collected_items:
            print("Item coletado!")

        # Desenhar na tela
        screen.fill(WHITE)
        collectibles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
