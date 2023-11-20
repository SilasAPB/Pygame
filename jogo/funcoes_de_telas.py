import pygame
from os import path

from jogo1 import *
from config import *




def init_screen(window):
    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont('lucidaconsola',35) 
    text = smallfont.render('JOGAR' , True , BLUE)



    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background=pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    pygame.mixer.music.load(os.path.join(SND_DIR, 'music.mp3'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    running = True
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH/2-100 <= mouse[0] <= WIDTH/2+100 and HEIGHT/2-30 <= mouse[1] <= HEIGHT/2+30:
                    state=MAPS
                    running=False

        window.fill(BLACK)
        window.blit(background,background_rect)

        mouse=pygame.mouse.get_pos()
        
        if WIDTH/2-100 <=   mouse[0] <= WIDTH/2+100 and HEIGHT/2-30 <= mouse[1] <= HEIGHT/2+30:
            pygame.draw.rect(window,WHITE,[WIDTH/2-100,HEIGHT/2-30,200,60]) 
          
        else: 
            pygame.draw.rect(window, BLACK,[WIDTH/2-100,HEIGHT/2-30,200,60])

        
        window.blit(text, (WIDTH/2-50, HEIGHT/2-15))

        pygame.display.update()

    pygame.mixer.music.unload()
    return state

def end_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

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

            if event.type == pygame.KEYUP:
                state = INIT
                running = False

        # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        window.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    pygame.mixer.music.unload()
    return state




def map_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont('lucidaconsola',35) 
    text = smallfont.render('JOGAR' , True , BLUE)

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'escolha_mapa.png')).convert()
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH/4-140 <=   mouse[0] <= WIDTH/4+140 and HEIGHT/4-30 <= mouse[1] <= HEIGHT/4+30:
                    state=GAME
                    running=False   
                if 3*WIDTH/4-140 <=   mouse[0] <= 3*WIDTH/4+140 and HEIGHT/4-30 <= mouse[1] <= HEIGHT/4+30:
                    state=GAME
                    running=False   
                if 3*WIDTH/4-140 <=   mouse[0] <= 3*WIDTH/4+140 and 3*HEIGHT/4-30 <= mouse[1] <= 3*HEIGHT/4+30:
                    state=GAME
                    running=False   
                if WIDTH/4-140 <=   mouse[0] <= WIDTH/4+140 and 3*HEIGHT/4-30 <= mouse[1] <= 3*HEIGHT/4+30:
                    state=GAME
                    running=False   

        # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        window.blit(background, background_rect)

        mouse=pygame.mouse.get_pos()
        
        if WIDTH/4-140 <=   mouse[0] <= WIDTH/4+140 and HEIGHT/4-30 <= mouse[1] <= HEIGHT/4+30:
            pygame.draw.rect(window,WHITE,[WIDTH/4-100,HEIGHT/4-30,200,60])   
        else: 
            pygame.draw.rect(window, BLACK,[WIDTH/4-100,HEIGHT/4-30,200,60])

        if 3*WIDTH/4-140 <=   mouse[0] <= 3*WIDTH/4+140 and HEIGHT/4-30 <= mouse[1] <= HEIGHT/4+30:
            pygame.draw.rect(window,WHITE,[3*WIDTH/4-100,HEIGHT/4-30,200,60])   
        else: 
            pygame.draw.rect(window, BLACK,[3*WIDTH/4-100,HEIGHT/4-30,200,60])

        if 3*WIDTH/4-140 <=   mouse[0] <= 3*WIDTH/4+140 and 3*HEIGHT/4-30 <= mouse[1] <= 3*HEIGHT/4+30:
            pygame.draw.rect(window,WHITE,[3*WIDTH/4-100,3*HEIGHT/4-30,200,60])   
        else: 
            pygame.draw.rect(window, BLACK,[3*WIDTH/4-100,3*HEIGHT/4-30,200,60])

        if WIDTH/4-140 <=   mouse[0] <= WIDTH/4+140 and 3*HEIGHT/4-30 <= mouse[1] <= 3*HEIGHT/4+30:
            pygame.draw.rect(window,WHITE,[WIDTH/4-100,3*HEIGHT/4-30,200,60])   
        else: 
            pygame.draw.rect(window, BLACK,[WIDTH/4-100,3*HEIGHT/4-30,200,60])

        
        window.blit(text, (WIDTH/4-50, HEIGHT/4-15))
        window.blit(text, (3*WIDTH/4-50, 3*HEIGHT/4-15))
        window.blit(text, (WIDTH/4-50, 3*HEIGHT/4-15))
        window.blit(text, (3*WIDTH/4-50, HEIGHT/4-15))



        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    pygame.mixer.music.unload()
    return state






        

        