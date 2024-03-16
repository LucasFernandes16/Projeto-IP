#função responsável por mover nosso personagem principal na tela 
def handle_move(player):
    keys = pygame.key.get_pressed() #informa todas as teclas que estão sendo pressionadas no comento 
    player.x_vel = 0 
    #criando a responsividade para apertar a tecla e mover o personagem
    if keys[pygame.K_LEFT]: 
        player.move_left(PLAYER_VEL) # passando o quanto o player vai se mover 
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)  

# criando a função que vai fazer o boneco pular 
def jump(self):
        self.y_vel = -self.GRAVITY * 7 #a gravidade vai negativa para que ele pule no ar, ou seja fique mais "leve" e vá para cima
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0 #isso faz com que quando eu pule consiga me livrar da gravidade   
#####opa opa opaaa 
            

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png") # bg_image é a imagem de fundo 

    block_size = 96

    player = Player(100, 100, 50, 50)
    
    fire = Fire(750, HEIGHT - block_size*5 - 64, 16, 32)
    fire.on()
    fire1 = Fire(180, HEIGHT - block_size - 64 , 16, 32)
    fire1.on()

    
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),  
               Block(block_size * 3, HEIGHT - block_size * 3.5, block_size), fire,fire1,
               Block(block_size * 6,HEIGHT - block_size * 5,block_size),Block(block_size * 7,HEIGHT - block_size * 5,block_size),Block(block_size * 8,HEIGHT - block_size * 5,block_size),Block(block_size * 9,HEIGHT - block_size * 5,block_size)
               ,Block(block_size * 12, HEIGHT - block_size * 6, block_size)]
    
    
    offset_x = 0
    scroll_area_width = 200

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
        fire.loop()
        fire1.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x) #chamando a def do fundo 

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()