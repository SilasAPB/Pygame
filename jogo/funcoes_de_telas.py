import pygame
from os import path

from jogo1 import *
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



def end_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'fim.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = INIT
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state






        