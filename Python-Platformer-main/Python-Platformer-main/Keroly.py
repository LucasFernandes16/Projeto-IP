import pygame
from os import listdir
from os.path import isfile, join
from pygame.locals import *
pygame.init()

pygame.display.set_caption("MENU INICIAL")

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

cor = (255, 255, 255) # cor em rgb
window.fill(cor)# pinta a tela toda com a cor desejada
pygame.display.flip()# atualiza a atela 

fonte = pygame.font.Font(None, 36)# dertermina o tipo da fonte e o tamanho usado para escrever a "insrtrucao"


def  exibir_instrucoes():# funçao q exibira na tela a instruçao de inicializaçao do jogo
    instrucoes_texto = fonte.render("Pressione qualquer tecla para iniciar", True, (0, 0, 0))# a string a ser "printada", a cor da string na tela em rgb
    x_texto = (WIDTH -  instrucoes_texto.get_width()) // 2# a dimensao x da instruçao que aparecerá na tela para deixa  centralzada
    y_texto = (HEIGHT -  instrucoes_texto.get_height()) // 2 # a dimensao y da instruçao que aparecá na tela pra deixar centralizada
    window.blit(instrucoes_texto, (x_texto,y_texto)) # as especificaçoes das string e a sua coordenada na tela 
    pygame.display.flip() # atualiza a tela 



while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:# detecta quando o jogador sai do jogo
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:# detecta q o jogador apertou alguma tecla e iniciará o jogo
            # o processo a baixo é so um teste que mudara a cor da tela ao detectar q alguma tecla foi apertada
            cor = (0, 255, 0)
            window.fill(cor)
            pygame.display.flip()

    exibir_instrucoes()
    # fyfyhfyu