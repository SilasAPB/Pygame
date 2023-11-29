import pygame
from os import path

from jogo1 import *
from config import *
from lista_assests import *


# Tela do jogo de escolha de mapa
def map_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets=load_assets()

    smallfont = pygame.font.SysFont('bookantiqua',26) 
    text1 = smallfont.render('Templo Guangzhou', True , WHITE)
    text2 = smallfont.render('Jardins Cristalinos' , True , WHITE)
    text3 = smallfont.render('Canyon dos Esquecidos' , True , WHITE)
    text4 = smallfont.render('Beco do Coringa' , True , WHITE)

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'escolha_mapa.png')).convert()
    background=pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    
    pygame.mixer.music.load(os.path.join(SND_DIR, 'map.wav'))
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
                if WIDTH/8-10 <=   mouse[0] <= WIDTH/8+MIN_MAP_W+10 and HEIGHT/8-10 <= mouse[1] <= HEIGHT/8+MIN_MAP_H+10:
                    state=GAME1
                    running=False
                    print("Jogo 1") 
                if 5*WIDTH/8-10 <=   mouse[0] <= 5*WIDTH/8+MIN_MAP_W+10 and HEIGHT/8-10 <= mouse[1] <= HEIGHT/8+MIN_MAP_H+10:
                    state=GAME2
                    running=False
                    print("Jogo 2")
                if 5*WIDTH/8-10 <=   mouse[0] <= 5*WIDTH/8+MIN_MAP_W+10 and 5*HEIGHT/8-10 <= mouse[1] <= 5*HEIGHT/8+MIN_MAP_H+10:
                    state=GAME4    
                    running=False
                    print("Jogo 3")    
                if WIDTH/8-10 <=   mouse[0] <= WIDTH/8+MIN_MAP_W+10 and 5*HEIGHT/8-10 <= mouse[1] <= 5*HEIGHT/8+MIN_MAP_H+10:
                    state=GAME3
                    running=False
                    print("Jogo 4")    

        # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        window.blit(background, background_rect)

        mouse=pygame.mouse.get_pos() #pega a posição do mouse
        
        #DESENHA O BOTÂO 1
        if WIDTH/8-10 <=   mouse[0] <= WIDTH/8+MIN_MAP_W+10 and HEIGHT/8-10 <= mouse[1] <= HEIGHT/8+MIN_MAP_H+10:
            pygame.draw.rect(window,WHITE,[WIDTH/8-10,HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)   #Aceso
        else: 
            pygame.draw.rect(window, BLACK,[WIDTH/8-10,HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)#Apagado
          
        #DESENHA O BOTÂO 2
        if 5*WIDTH/8-10 <=   mouse[0] <= 5*WIDTH/8+MIN_MAP_W+10 and HEIGHT/8-10 <= mouse[1] <= HEIGHT/8+MIN_MAP_H+10:
            pygame.draw.rect(window,WHITE,[5*WIDTH/8-10,HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)   #Aceso
        else: 
            pygame.draw.rect(window, BLACK,[5*WIDTH/8-10,HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)#Apagado
          
          
        #DESENHA O BOTÂO 3
        if WIDTH/8-10 <=   mouse[0] <= WIDTH/8+MIN_MAP_W+10 and 5*HEIGHT/8-10 <= mouse[1] <= 5*HEIGHT/8+MIN_MAP_H+10:
            pygame.draw.rect(window,WHITE,[WIDTH/8-10,5*HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)   #Aceso
        else: 
            pygame.draw.rect(window, BLACK,[WIDTH/8-10,5*HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)#Apagado
          
          
        #DESENHA O BOTÂO 4
        if 5*WIDTH/8-10 <=   mouse[0] <= 5*WIDTH/8+MIN_MAP_W+10 and 5*HEIGHT/8-10 <= mouse[1] <= 5*HEIGHT/8+MIN_MAP_H+10:
            pygame.draw.rect(window,WHITE,[5*WIDTH/8-10,5*HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)   #Aceso
        else: 
            pygame.draw.rect(window, BLACK,[5*WIDTH/8-10,5*HEIGHT/8-10,MIN_MAP_W+20,MIN_MAP_H+20],border_radius=12)#Apagado
          
        window.blit(assets[MINIMAP1_IMG], (WIDTH/8,HEIGHT/8))
        window.blit(assets[MINIMAP2_IMG], (5*WIDTH/8,HEIGHT/8))
        window.blit(assets[MINIMAP3_IMG], (5*WIDTH/8,5*HEIGHT/8))
        window.blit(assets[MINIMAP4_IMG], (WIDTH/8,5*HEIGHT/8))

        
        window.blit(text1, (WIDTH/8+50, HEIGHT/4+100))
        window.blit(text2, (5*WIDTH/8+55, HEIGHT/4+100))
        window.blit(text3, (WIDTH/8+20, 3*HEIGHT/4-135))
        window.blit(text4, (5*WIDTH/8+65, 3*HEIGHT/4-135))
 



        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    pygame.mixer.music.unload()
    return state