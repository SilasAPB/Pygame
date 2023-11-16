import pygame
from os import path

from jogo1 import *
from config import *




def init_screen(window):
    clock = pygame.time.Clock()

    # fonte  = pygame.font.Font(None,32)
    # user_text = 'BEM VINDO AO JOGO!'

    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:

        clock.tick(FPS)
        # np1 = 'Qual nome você gostaria de dar ao seu personagem? '
        # np2 = 'Qual nome você gostaria de dar ao seu personagem? '
        # text_sufrace = fonte.render(user_text,True,(0,255,0))
        # text_nome1 = fonte.render(np1,True,(255,255,255))
        # text_nome2 = fonte.render(np2,True,(255,255,255))

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        window.fill(BLACK)
        window.blit(background,background_rect)
        # window.blit(text_sufrace,(50,50))
        # window.blit(text_nome1,(10,15))
        # window.blit(text_nome2,(13,15))

        pygame.display.flip()

    return state
    



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






        