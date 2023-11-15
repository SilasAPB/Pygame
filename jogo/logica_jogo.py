from config import *
import pygame,sys
from funcoes_de_telas import *


pygame.init()






window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SandmannVille: Terra de Faroeste')




pygame.display.set_caption('SandmannVille: Terra de Faroeste')

lista_assets = [backgroud,player_1_img,player_2_img,block_1_img,block_2_img,img_bala,img_bar]
state = INIT
while state != QUIT :
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = jogo_principal(window,lista_assets)
    else:
        state = end_screen(window)
