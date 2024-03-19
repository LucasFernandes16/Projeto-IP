import pygame
from Player import *
from Objects import *


PLAYER_VEL = 5

def collectible_vertical_collision(player, collectible, dy):
    collided_collectible = []
    for obj in collectible:
        if pygame.sprite.collide_mask(player, obj): # Pela herança da classe sprite.Sprite usamos a "mask" dela para facilitar a nossa colisão
        # Passamos o nosso player e os objetos q iremos colidir
            if dy > 0:
                player.rect.bottom = obj.rect.top
            elif dy < 0:
                player.rect.top = obj.rect.bottom
            
            collided_collectible.append(obj)

    return collided_collectible

def collectible_collide(player, collectible, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in collectible:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            #break

    #player.move(-dx, 0)
    player.update()
    return collided_object



# Função responsável por mover nosso personagem principal na tela
def collectible_handle_move(player, collectible):
    keys = pygame.key.get_pressed() #informa todas as teclas que estão sendo pressionadas no comento 

    player.x_vel = 0
    collide_left = collectible_collide(player, collectible, -PLAYER_VEL * 2)
    collide_right = collectible_collide(player, collectible, PLAYER_VEL * 2)
    # criando a responsividade para apertar a tecla e mover o personagem
    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL) # passando o quanto o player vai se mover
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = collectible_vertical_collision(player, collectible, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "flag":
            Flag.hit_flag()