from config import INIT,GAME,QUIT
import pygame,sys
from funcoes_de_telas import *
import jogo1





while state != QUIT :
    if state == INIT:
        state = init_screen(jogo1.window)
    elif state == GAME:
        pass
        #state = game_screen(window)
    else:
        state = final_screen(jogo1.window)
