from config import *
import pygame,sys
from funcoes_de_telas import init_screen,end_screen,map_screen
from classes import *
from jogo1 import jogo_principal



pygame.init()
pygame.mixer.init()


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SandmannVille: Terra de Faroeste')


state = INIT
while state != QUIT :
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = jogo_principal(window)
    elif state == OVER:
        state = end_screen(window)
    elif state == MAPS:
        state = map_screen(window)
    else:
        state=QUIT


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizadosr
