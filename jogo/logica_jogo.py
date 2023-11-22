from config import *
import pygame,sys
from funcoes_de_telas import init_screen,end_screen,map_screen
from classes import *
from jogo1 import jogo_principal



pygame.init()
pygame.mixer.init()


window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('SandmannVille: Terra de Faroeste')



state = INIT
while state != QUIT :
    if state == INIT:
        state = init_screen(window)
    elif state == GAME1:
        state = jogo_principal(window,1)
    elif state == GAME2:
        state = jogo_principal(window,2)
    elif state == GAME3:
        state = jogo_principal(window,3)
    elif state == GAME4:
        state = jogo_principal(window,4)
    elif state == OVER:
        state = end_screen(window)
    elif state == MAPS:
        state = map_screen(window)
    else:
        state=QUIT


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizadosr
