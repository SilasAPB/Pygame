import pygame
from os import path

from jogo1 import *
from config import *
from lista_assests import *


def person_screen(window):
    clock = pygame.time.Clock()


    smallfont = pygame.font.SysFont('lucidaconsola',40) 
    texto_p1 = smallfont.render('Player 1: escolha seu personagem com as teclas W,A,S,D' , True , RED)
    texto_p2 = smallfont.render('Player 2: escolha seu personagem com as setas no canto inferior do teclado.', True , BLUE)




    background = pygame.image.load(path.join(IMG_DIR, 'escolha_mapa.png')).convert()
    background=pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    

    pygame.mixer.music.load(os.path.join(SND_DIR, 'person.mp3'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=0)

    Choose1=0
    Choose2=0

    running=0
    while running<2:
        
        clock.tick(FPS)

        assets=load_assets()

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = 2

            if event.type==pygame.KEYDOWN:
                if Choose1==0:
                    if event.key == pygame.K_a:
                        Choose1=1
                        running+=1
                    elif event.key == pygame.K_w:
                        Choose1=2
                        running+=1
                    elif event.key == pygame.K_d:
                        Choose1=3
                        running+=1
                    elif event.key == pygame.K_s:
                        Choose1=4
                        running+=1

                if Choose2==0:
                    if event.key == pygame.K_LEFT:
                        Choose2=1
                        running+=1
                    elif event.key == pygame.K_UP:
                        Choose2=2
                        running+=1
                    elif event.key == pygame.K_RIGHT:
                        Choose2=3
                        running+=1
                    elif event.key == pygame.K_DOWN:
                        Choose2=4
                        running+=1

        window.fill(BLACK)
        window.blit(background, background_rect)


        window.blit(assets[PLAYER1_IMG], (WIDTH/8,HEIGHT/8))
        window.blit(assets[PLAYER3_IMG], (5*WIDTH/8,HEIGHT/8))
        window.blit(assets[PLAYER4_IMG], (5*WIDTH/8,5*HEIGHT/8))
        window.blit(assets[PLAYER5_IMG], (WIDTH/8,5*HEIGHT/8))
        window.blit(texto_p1,(5,HEIGHT-30))
        window.blit(texto_p2,(5,HEIGHT-70))
    


        pygame.display.flip()



    state=MAPS

    lis=[state,Choose1,Choose2]

    pygame.mixer.music.unload()
    return lis