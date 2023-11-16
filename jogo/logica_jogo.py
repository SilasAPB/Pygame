from config import *
import pygame, sys
from funcoes_de_telas import *
from jogo1 import *




state = INIT
while state != QUIT :
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        pass
        #state = game_screen(window)
    elif state== OVER:
        state = end_screen(window)
