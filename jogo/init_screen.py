import pygame
from os import path

from jogo1 import *
from config import *
from lista_assests import *




def init_screen(window):
    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont('lucidaconsola',25) 
    text = smallfont.render('JOGAR' , True , BLUE)
    text_rect=text.get_rect(center=(WIDTH/2,HEIGHT/2))

    

    texto_explicacaop1 = smallfont.render('Player 1: Jogador da esquerda' , True , RED)
    texto_explicacaop2 = smallfont.render('Player 2: Jogador da direita' , True , BLUE)



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
                    state=PLAYERS
                    running=False

        window.fill(BLACK)
        window.blit(background,background_rect)

        mouse=pygame.mouse.get_pos()
        
        if WIDTH/2-100 <=   mouse[0] <= WIDTH/2+100 and HEIGHT/2-30 <= mouse[1] <= HEIGHT/2+30:
            pygame.draw.rect(window,WHITE,[WIDTH/2-100,HEIGHT/2-30,200,60],border_radius=20) 
          
        else: 
            pygame.draw.rect(window, BLACK,[WIDTH/2-100,HEIGHT/2-30,200,60],border_radius=20)

        
        window.blit(text,text_rect)
        window.blit(texto_explicacaop1,(30,HEIGHT - 50))
        window.blit(texto_explicacaop2,(30,HEIGHT - 30))




        pygame.display.update()

    pygame.mixer.music.unload()
    return state










        

        