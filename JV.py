
class moving_player:
    #função responsável por mover nosso personagem principal na tela 
    def move(player):
        keys = pygame.key.get_pressed() #informa todas as teclas que estão sendo pressionadas no comento 
        player.x_vel=0 
        #criando a responsividade para apertar a tecla e mover o personagem
        if keys[pygame.K_left]: 
            player.move_left(PLAYER_VEL) # passando o quanto o player vai se mover 
        if keys[pygame.R_left]:
            player.move_right(PLAYER_VEL)