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