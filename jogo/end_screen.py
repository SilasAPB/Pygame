import pygame
from os import path

from jogo1 import *
from config import *
from lista_assests import *


def end_screen(window,ganhador,g_img):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    gritante = pygame.font.SysFont('twcennegrito',70)
    gritante_mini = pygame.font.SysFont('twcen',20)
    smallfont = pygame.font.SysFont('couriernew',30) 
    text = smallfont.render('Aperte R para jogar novamente ou ESC para sair do jogo' , True , BLACK)
    text_up = gritante.render(f'VITORIA ROYALE: {ganhador} ' , True , BLACK)
    text_up_sub=gritante_mini.render('Parabéns, o ar condicionado é todo seu!' , True , BLACK)

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'fim.png')).convert()
    background=pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    
    pygame.mixer.music.load(os.path.join(SND_DIR, 'omago.mp3'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=0)

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    state = INIT
                    running = False
                if event.key == pygame.K_ESCAPE: 
                    state = QUIT
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        window.fill(WHITE)
        window.blit(g_img, (WIDTH/2-PLAYERS_WIDTH_L/2,HEIGHT/2-PLAYERS_HEIGHT_L/2))
        # window.blit(background, background_rect)

        window.blit(text, (130, HEIGHT-100))
        window.blit(text_up, (WIDTH/2-300, HEIGHT/8))
        window.blit(text_up_sub, (WIDTH/2-300, HEIGHT/8+70))
       

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    pygame.mixer.music.unload()
    return state

