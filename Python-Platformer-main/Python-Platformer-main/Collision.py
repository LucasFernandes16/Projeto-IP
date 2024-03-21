import pygame
from Player import *

PLAYER_VEL = 5

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj): # Pela herança da classe sprite.Sprite usamos a "mask" dela para facilitar a nossa colisão
        # Passamos o nosso player e os objetos q iremos colidir
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects

def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object

# Função responsável por mover nosso personagem principal na tela
def handle_move(player, objects):
    keys = pygame.key.get_pressed() #informa todas as teclas que estão sendo pressionadas no comento 

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)
    # criando a responsividade para apertar a tecla e mover o personagem
    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL) # passando o quanto o player vai se mover
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()
        if obj and obj.name == "spike":
            player.make_hit()
        