import pygame
from os import path

from jogo1 import *
from config import *
from lista_assests import *


def person_screen(window):
    clock = pygame.time.Clock()

    #TEXTOS PARA AUXILIAR NA ESCOLHA DO PERSONAGEM  
    smallfont = pygame.font.SysFont('lucidaconsola',40) 
    texto_p1 = smallfont.render('Player 1: escolha seu personagem com as teclas W,A,S,D' , True , RED)
    texto_p2 = smallfont.render('Player 2: escolha seu personagem com as setas no canto inferior do teclado.', True , BLUE)

    #CORES E STRINGS QUE QUEREM SER INSERIDAS NA TELAS(AS MENSAGENS PARA AUXILIAR O JOGADOR)
    textop1_a = smallfont.render('P1: A', True , RED)
    textop2_left = smallfont.render('P2:  <-', True , BLUE)

    textop1_w = smallfont.render('P1: W', True , RED)
    arrow_up = smallfont.render('^', True , BLUE)
    textop2_up = smallfont.render('P2: |', True , BLUE)

    textop1_d = smallfont.render('P1: D', True , RED)
    textop2_right = smallfont.render('P2: ->', True , BLUE)

    textop1_s = smallfont.render('P1: S', True , RED)
    arrow_down = smallfont.render('v', True , BLUE)
    textop2_down = smallfont.render('P2: |', True , BLUE)
    


    background = pygame.image.load(path.join(IMG_DIR, 'escolha_mapa.png')).convert()#ADICIONA A IMAGEM 
    background=pygame.transform.scale(background, (WIDTH, HEIGHT)) #CONVERTE PARA A ESCALA ESCOLHIDA
    background_rect = background.get_rect() # TRANSFORMA A IMAGEM NUM RETANGULO
    
    # ADICIONA MUSICA AO JOGO
    pygame.mixer.music.load(os.path.join(SND_DIR, 'person.mp3'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=0)

    state=PLAYERS

    Choose1=0
    Choose2=0

    running=0
    #LOOP DA SELEÇÃO DOS PERSONAGENS
    while running<3:
        
        clock.tick(FPS)

        assets=load_assets()

        for event in pygame.event.get():
            # VERIFICA SE O JOGO FOI FECHADO.
            if event.type == pygame.QUIT:
                state = QUIT
                running = 3

            #VERIFICA SE ALGUM BOTÃO FOI CLICADO
            if event.type==pygame.KEYDOWN:
                if Choose1==0:
                    #VERIFICA QUAL BOTÃO FOI CLICADO
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
                
                if Choose2!=0 and Choose1!=0:
                    if event.key == pygame.K_SPACE:
                        running+=1
                    if event.key == pygame.K_b:
                        running=0
                        Choose1=0
                        Choose2=0

        #DEFINE O FUNDO DA COR PRETA E ADICIONA O FUNDO NO JOGO
        window.fill(BLACK)
        window.blit(background, background_rect)


        if Choose1==1 and Choose2!=1:
            pygame.draw.rect(window,RED,[2*WIDTH/8,(HEIGHT/8)+30,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)   #Aceso
        elif Choose2==1 and Choose1!=1: 
            pygame.draw.rect(window, BLUE,[2*WIDTH/8,(HEIGHT/8)+30,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado
        elif Choose2==1 and Choose1==1: 
            pygame.draw.rect(window, PURPLE,[2*WIDTH/8,(HEIGHT/8)+30,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado

        if Choose1==2 and Choose2!=2:
            pygame.draw.rect(window,RED,[6*WIDTH/8,(HEIGHT/8)+30,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)   #Aceso
        elif Choose2==2 and Choose1!=2: 
            pygame.draw.rect(window, BLUE,[6*WIDTH/8,(HEIGHT/8)+30,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado
        elif Choose2==2 and Choose1==2: 
            pygame.draw.rect(window, PURPLE,[6*WIDTH/8,(HEIGHT/8)+30,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado
          
        #DESENHA O BOTÂO 3
        if Choose1==3 and Choose2!=3:
            pygame.draw.rect(window,RED,[6*WIDTH/8,(5*HEIGHT/8)+10,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)   #Aceso
        elif Choose2==3 and Choose1!=3: 
            pygame.draw.rect(window, BLUE,[6*WIDTH/8,(5*HEIGHT/8)+10,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado
        elif Choose2==3 and Choose1==3: 
            pygame.draw.rect(window, PURPLE,[6*WIDTH/8,(5*HEIGHT/8)+10,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado
          
          
        #DESENHA O BOTÂO 4
        if Choose1==4 and Choose2!=4:
            pygame.draw.rect(window,RED,[5*2*WIDTH/8,(5*HEIGHT/8)+10,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)   #Aceso
        elif Choose2==4 and Choose1!=4: 
            pygame.draw.rect(window, BLUE,[5*2*WIDTH/8,(5*HEIGHT/8)+10,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado
        elif Choose2==4 and Choose1==4: 
            pygame.draw.rect(window, PURPLE,[5*2*WIDTH/8,(5*HEIGHT/8)+10,PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L],border_radius=12)#Apagado
          

        #COLOCA A IMAGEM DOS PLAYERS PARA A SELEÇÃO DOS RESPECTIVOS NA POSIÇÃO DE INTERESSE
        window.blit(assets[PLAYER1_IMG_L], (2*WIDTH/8,(HEIGHT/8)+30))
        window.blit(textop1_a,((WIDTH/8)- 50,(HEIGHT/8)-60))
        window.blit(textop2_left,((WIDTH/8)-50,(HEIGHT/8)-20))
        
        window.blit(assets[PLAYER2_IMG_L], (6*WIDTH/8,(HEIGHT/8)+30))
        window.blit(textop1_w,(((5*WIDTH/8)-50,(HEIGHT/8)-60)))
        window.blit(arrow_up,((5*WIDTH/8)-4,(HEIGHT/8)-20))
        window.blit(textop2_up,((5*WIDTH/8)-50,(HEIGHT/8)-20))

        window.blit(assets[PLAYER3_IMG_L], (6*WIDTH/8,(5*HEIGHT/8)+10))
        window.blit(textop1_d,((5*WIDTH/8)-50,(5*HEIGHT/8)-70))
        window.blit(textop2_right,(((5*WIDTH/8)-50,(5*HEIGHT/8)-40)))

        window.blit(assets[PLAYER4_IMG_L], (2*WIDTH/8,(5*HEIGHT/8)+10))
        window.blit(textop1_s,((WIDTH/8)-51,(5*HEIGHT/8)-70))
        window.blit(arrow_down,((WIDTH/8)-3,(5*HEIGHT/8)-19))
        window.blit(textop2_down,((WIDTH/8)-48.5,(5*HEIGHT/8)-35))


        window.blit(texto_p1,(5,HEIGHT-70))
        window.blit(texto_p2,(5,HEIGHT-30))
    




        #UPDATE DA PÁGINA
        pygame.display.flip()


    #FAZ COM QUE A VARIAVEL QUE ESTÁ NA LÓGICA DO JOGO DIRECIONE O JOGO PARA A TELA DE MAPAS
    if state!= QUIT:
        state=MAPS

    #GUARDA O "MOMENTO" (STATE) QUE O JOGO ESTÁ E OS PERSONAGENS QUE FORAM ESCOLHIDOS PELAS PESSOAS QUE ESTÃO JOGANDO
    lis=[state,Choose1,Choose2]

    pygame.mixer.music.unload()
    return lis