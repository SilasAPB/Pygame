# ===== Inicialização =====
# ----- Importa e inicia pacotes
#from typing import Any
import pygame,os,sys
from math import sin,cos


from config import *
from classes import *
from lista_assests import *


# ===== Loop principal =====
def jogo_principal(window,tela):
    clock=pygame.time.Clock()

    assets = load_assets()

    game = True

    playerControls={
    'p1' : [pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_r,pygame.K_q], #humberto
    'p2' : [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_RSHIFT,pygame.K_SLASH]#dani
    
    }
# ----- Criando um grupo de sprites(que vai agir/atualizar conforme o tempo)
    all_sprites=pygame.sprite.Group()
    all_players=pygame.sprite.Group()
    all_obstaculos=pygame.sprite.Group()
    all_bullets=pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_players'] = all_players
    groups['all_bullets'] = all_bullets
    groups['all_obstaculos'] = all_obstaculos



    player1=Player('P1',assets[PLAYER1_IMG],WIDTH/4,HEIGHT-PLAYERS_HEIGHT/2,groups,assets,playerControls['p1']) #adicionando jogador ao jogo
    player2=Player('P2',assets[PLAYER2_IMG],WIDTH*3/4,HEIGHT-PLAYERS_HEIGHT/2,groups,assets,playerControls['p2'])
    plataforma1=Block(assets[BLOCK1_IMG],600,HEIGHT)
    plataforma2=Block(assets[BLOCK2_IMG],BLOCK_WIDTH,400)

    health_bar1 = HealthBar(10, 10, 150, 30, player1)

    health_bar2 = HealthBar(WIDTH-160, 10, 150, 30, player2)


    all_sprites.add(player1)
    all_sprites.add(player2) # Adicionando jogador ao grupo de sprites
    all_sprites.add(plataforma1)
    all_sprites.add(plataforma2)

    all_players.add(player1)
    all_players.add(player2)
    all_obstaculos.add(plataforma1)
    all_obstaculos.add(plataforma2)

        
    pygame.mixer.music.load(os.path.join(SND_DIR, 'crack.mp3'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    
    while game:
        clock.tick(FPS)

        Sair=0
    # ----- Trata eventos
        for event in pygame.event.get():
            
            # ----- Verifica se usuário fechou o jogo
            if event.type == pygame.QUIT:
                Sair=1
                game = False
                
            # ----- Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # ----- Dependendo da tecla, altera a velocidade.
                for plr in all_players:
                    if event.key == plr.playerControls[0]:  # Left
                        plr.speedx -= PLAYERS_VELOCITY
                        plr.playerDirection = -1
                    if event.key == plr.playerControls[1]:  # Right
                        plr.speedx += PLAYERS_VELOCITY
                        plr.playerDirection = +1
                    if event.key == plr.playerControls[2] and plr.jump==True:  # Up
                        plr.jump = False
                        plr.speedy -= PLAYER_JUMP
                    if event.key == plr.playerControls[4]:  # Shift
                        plr.firing = True
                    if event.key == plr.playerControls[5]:
                        plr.setImmortal(TEMPO_SEM_DANO)


                # ----- Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                for plr in all_players:
                    if event.key == plr.playerControls[0]:
                        plr.speedx = 0
                    if event.key == plr.playerControls[1]:
                        plr.speedx = 0
                    if event.key == plr.playerControls[4]:  # Shift
                        plr.firing = False



            # ----- Colisão entre players e projetis
        hit = pygame.sprite.groupcollide(all_players,all_bullets,False,True,pygame.sprite.collide_mask)
        if len(hit)>0:
            vidap1=1
            vidap2=1
            for player in hit.keys():
                if player == player1:
                    vidap1 = player1.nivel_vida(DANO_ARMA_1)
                    health_bar1.update(vidap1)
                elif player == player2:
                    vidap2 = player2.nivel_vida(DANO_ARMA_1)
                    health_bar2.update(vidap2)
            
            # se um morrer, o outro não morre
            if vidap1 == 0 :
                player1.kill()
                all_players.remove(player2)
                game=False
                
            elif vidap2 == 0:
                player2.kill()
                all_players.remove(player1)
                game=False
            



        all_sprites.update() # Atualiza a posição dos sprites(objetos)

        # ----- Gera saídas
        window.fill((0, 0, 255))  # Preenche com a cor branca

        if tela==1:
            window.blit(assets[BACKGROUND], (0,0)) # Nosso Fundo do mapa 1
        if tela==2:
            window.blit(assets[BACKGROUND2], (0,0)) # Nosso Fundo do mapa 2
        if tela==3:
            window.blit(assets[BACKGROUND4], (0,0)) # Nosso Fundodo mapa 3
        if tela==4:
            window.blit(assets[BACKGROUND3], (0,0)) # Nosso Fundo do mapa 4


        health_bar1.draw(window)
        health_bar2.draw(window)


        all_sprites.draw(window) # ----- Desenha os sprites(objetos) na tela

        # ----- Atualiza estado do jogo
        pygame.display.update()
        clock.tick(FPS)  # Mostra o novo frame para o jogador

    if Sair==1:
        state=QUIT
    else:
        pygame.mixer.music.unload()
        state=OVER
    return state