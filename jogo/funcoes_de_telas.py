import pygame
from jogo import *
from config import *
pygame.init()
def init_screen(window):
    clock = pygame.time.Clock()
    fonte  = pygame.font.Font(None,32)
    user_text = 'BEM VINDO AO JOGO!'
    np1 = ''
    np2 = ''
    while np1 != ('').strip and np2 != ('').strip:
        np1 = input('Qual nome você gostaria de dar ao seu personagem? ')
        np2 = input('Qual nome você gostaria de dar ao seu personagem? ')
        window.fill((0,0,0))
        text_sufrace = fonte.render(user_text,True,(0,255,0))
        text_nome1 = fonte.render(np1,True,(255,255,255))
        text_nome2 = fonte.render2(np2,True,(255,255,255))
        window.blit(text_sufrace,(50,50))
        window.blit(text_nome1,(10,15))
        window.blit(text_nome2,(13,15))

        pygame.display.flip()
        clock.tick(60)



def final_screen(window):
    pass





        