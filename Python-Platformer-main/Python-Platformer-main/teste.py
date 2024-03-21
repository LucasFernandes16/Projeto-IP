import os
import time
import pygame
from os import listdir
from os.path import isfile, join
from Objects import *
from Background import *
from Sprites import *
from Player import Player
from Collision import *
from Initialization import *

pygame.init()
pygame.display.set_caption("Platformer")
pygame.mixer.init()

controle= 0
music = pygame.mixer.music.load(join("assets", "Music","metallica_fight_fire_with_fire.wav"))
pygame.mixer.music.play(-1)
a = True
def main(window):
    global controle
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png") # bg_image é a imagem de fundo 

    block_size = 96

    player = Player(100, 100, 50, 50)
    
    fire = Fire(750, HEIGHT - block_size*5 - 64, 16, 32)
    fire.on()
    
    spikes = Spikes(700, HEIGHT  - block_size*5 - 32 , 16, 16)



    flag = Flag(1155, HEIGHT - block_size*6 - 128 , 64, 64)
    
    # heart = Heart(1000, HEIGHT - block_size*4 - 32 , 16, 16)
    
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]

    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),  
               Block(block_size * 3, HEIGHT - block_size * 3.5, block_size), 
               fire,
               Block(block_size * 6,HEIGHT - block_size * 5,block_size),Block(block_size * 7,HEIGHT - block_size * 5,block_size),Block(block_size * 8,HEIGHT - block_size * 5,block_size),Block(block_size * 9,HEIGHT - block_size * 5,block_size)
               ,Block(block_size * 12, HEIGHT - block_size * 6, block_size)
               , Spikes(704, HEIGHT  - block_size*5 - 32 , 16, 16), Spikes(672, HEIGHT  - block_size*5 - 32 , 16, 16),Spikes(640, HEIGHT  - block_size*5 - 32 , 16, 16),Spikes(608, HEIGHT  - block_size*5 - 32 , 16, 16),Spikes(576, HEIGHT  - block_size*5 - 32 , 16, 16),Spikes(780, HEIGHT  - block_size*5 - 32 , 16, 16),Spikes(812, HEIGHT  - block_size*5 - 32 , 16, 16), Spikes(844, HEIGHT  - block_size*5 - 32 , 16, 16), Spikes(876, HEIGHT  - block_size*5 - 32 , 16, 16), Spikes(912, HEIGHT  - block_size*5 - 32 , 16, 16), Spikes(928, HEIGHT  - block_size*5 - 32 , 16, 16),]
    collectible= [flag]
    
    offset_x = 0
    scroll_area_width = 200

    run = True
    global a
    while run:
        a = True
        clock.tick(FPS)
        if pygame.sprite.collide_mask(player, flag):
            fundo=pygame.image.load(join("assets", "Screens", 'final_img.png'))
            window.blit(fundo, (0,0))
            pygame.display.update()
            a = False
            time.sleep(1)
            #run = False
        
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
           

            if event.type == pygame.KEYDOWN: #checando se tem uma tecla pressionada
                if event.key == pygame.K_SPACE and player.jump_count < 2: #se a tecla for espaço e o contador dos nossos pulos for menor que dois, vai poder pular duas vezes
                    player.jump()
                if player.alive == False and  event.key == pygame.K_RETURN:
                    main(window)
                if event.key == pygame.K_RETURN:
                    controle+=1
                    main(window)
                if event.key == pygame.K_RETURN and a == False and controle > 0:
                    main(window)
                
                
        
        if controle == 0:
            init_tela()
        else:

            flag.loop()
            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            #collectible_handle_move(player, collectible)
            draw(window, background, bg_image, player, objects, offset_x, collectible) #chamando a def do fundo 

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or ((player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)