from config import *
import pygame,sys
from init_screen import *
from classes import *
from jogo1 import jogo_principal
from person_screen import *
from end_screen import *
from map_screen import *


pygame.init() # dá inicio ao pygame
pygame.mixer.init()


window = pygame.display.set_mode((WIDTH, HEIGHT)) #Definição de tela do jogo
pygame.display.set_caption('Imperium') #Defini o nome da tela


state = INIT # define aonde o jogo começa
while state != QUIT :
    if state == INIT:
        state = init_screen(window) #tela de inicio 
    elif state == GAME1:
        lis = jogo_principal(window,1,choose1,choose2)#mapa 1
        state=lis[0]
        ganhador=lis[1]
        g_img=lis[2]
    elif state == GAME2:
        lis = jogo_principal(window,2,choose1,choose2)#mapa 2
        state=lis[0]
        ganhador=lis[1]
        g_img=lis[2]
    elif state == GAME3:
        lis = jogo_principal(window,3,choose1,choose2)#mapa 3
        state=lis[0]
        ganhador=lis[1]
        g_img=lis[2]
    elif state == GAME4:
        lis = jogo_principal(window,4,choose1,choose2)#mapa 4
        state=lis[0]
        ganhador=lis[1]
        g_img=lis[2]
    elif state == OVER:
        state = end_screen(window,ganhador,g_img) #tela do fim
    elif state == MAPS:
        state = map_screen(window) #tela de escolha do mapa
    elif state == PLAYERS:
        lis = person_screen(window) # tela de escolha do personagem
        state=lis[0]
        choose1=lis[1] #registro da escolha do jogador 1
        choose2=lis[2] #registro da escolha do jogador 1
    else:
        state=QUIT


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizadosr
