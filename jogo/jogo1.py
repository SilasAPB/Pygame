# ===== Inicialização =====
# ----- Importa e inicia pacotes
#from typing import Any
import pygame,os,json
from math import sin,cos


from config import *
from classes import *
from lista_assests import *



# ===== Loop principal =====
def jogo_principal(window,tela,choose1,choose2):
    clock=pygame.time.Clock()
    cont = 0
    assets = load_assets()

    game = True

    TimerFont = pygame.font.SysFont('twcennegrito',60)

    playerControls={
    'p1' : [pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_LSHIFT,pygame.K_q], 
    'p2' : [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_0,pygame.K_SPACE,pygame.K_SLASH]
    
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

    lista_p=[assets[PLAYER1_IMG_L],assets[PLAYER2_IMG_L],assets[PLAYER3_IMG_L],assets[PLAYER4_IMG_L]]#lista de imagens para personagens
    img1=choose1-1
    img2=choose2-1



    player1=Player('P1',lista_p[img1],WIDTH/4,HEIGHT-PLAYERS_HEIGHT/2,groups,assets,playerControls['p1'],choose1) #adicionando jogador ao jogo
    player2=Player('P2',lista_p[img2],WIDTH*3/4,HEIGHT-PLAYERS_HEIGHT/2,groups,assets,playerControls['p2'],choose2)
    # plataforma1=Block(assets[BLOCK1_MAP2],600,HEIGHT)
    # plataforma2=Block(assets[BLOCK2_MAP2],BLOCK_WIDTH,400)

    health_bar1 = HealthBar(10, 10, 150, 30, player1)

    health_bar2 = HealthBar(WIDTH-160, 10, 150, 30, player2)


    all_sprites.add(player1)
    all_sprites.add(player2) # Adicionando jogador ao grupo de sprites

    all_players.add(player1)
    all_players.add(player2)

        
    # pygame.mixer.music.load(os.path.join(SND_DIR, 'crack.mp3'))
    # pygame.mixer.music.set_volume(0.2)
    # pygame.mixer.music.play(loops=-1)
    w, h = pygame.display.get_surface().get_size()

    verticalOffset = h % BLOCK_SIZE - BLOCK_SIZE/2
    horizontalOffset = w % BLOCK_SIZE - BLOCK_SIZE/2

    # ----- Inicializa mapa
    mapas = ["Templo Guangzhou.json","Jardins Cristalinos.json","Beco do Coringa.json","Canyon dos Esquecidos.json"]
    print(mapas[tela-1])
    with open(os.path.join(path.dirname(__file__), 'assets', 'maps',mapas[tela-1])) as mapaJson:
        mapa = json.load(mapaJson)

    for ln in range(len(mapa)):
        for col in range(len(mapa[ln])):
            plataforma = 0
            if mapa[ln][col] == 1:
                plataforma = Block(assets[f'bloco1_mapa{tela}'],col*BLOCK_SIZE-horizontalOffset,ln*BLOCK_SIZE-verticalOffset)
            elif mapa[ln][col] == 2:
                plataforma = Block(assets[f'bloco2_mapa{tela}'],col*BLOCK_SIZE-horizontalOffset,ln*BLOCK_SIZE-verticalOffset)
            elif mapa[ln][col] == 3:
                plataforma = Block(assets[f'bloco1_mapa{tela}'],col*BLOCK_SIZE-horizontalOffset,ln*BLOCK_SIZE-verticalOffset)
            else: continue
            all_sprites.add(plataforma)
            all_obstaculos.add(plataforma)


    while game:
        clock.tick(FPS)

        Sair=0
    # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica se usuário fechou o jogo
            if event.type == pygame.QUIT:
                Sair=1
                game = False
                ganhador=0
                g_img=0
                
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
                    vidap1 = player1.nivel_vida(list(hit.values())[0][0].damage)
                    health_bar1.update(vidap1)
                elif player == player2:
                    vidap2 = player2.nivel_vida(list(hit.values())[0][0].damage)
                    health_bar2.update(vidap2)
            
            
            # se um morrer, o outro não morre
            if vidap1 == 0 :
                player1.kill()
                ganhador=player2.name
                g_img=player2.logo
                all_players.remove(player2)
                game=False
                
            elif vidap2 == 0:
                player2.kill()
                ganhador=player1.name
                g_img=player1.logo
                all_players.remove(player1)
                game=False
            

        cont += 2
        if cont == ITEM_SWAP_TIME*FPS:
            for p in all_players:
                p.item.kill()
                p.item = p.changeItem()
                all_sprites.add(p.item)
                
            cont = 0

        if cont < ITEM_SWAP_TIME*FPS*2/5:
            Timer = TimerFont.render(str(ITEM_SWAP_TIME-cont//FPS) , True , WHITE)
        elif cont < ITEM_SWAP_TIME*FPS*3/5:
            Timer = TimerFont.render(str(ITEM_SWAP_TIME-cont//FPS) , True , YELLOW)
        else:
            Timer = TimerFont.render(str(ITEM_SWAP_TIME-cont//FPS) , True , RED)




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




        
        all_sprites.draw(window) # ----- Desenha os sprites(objetos) na tela
        window.blit(Timer,(WIDTH/2,10))
        health_bar1.draw(window)
        health_bar2.draw(window)
        # ----- Atualiza estado do jogo
        pygame.display.update()
        clock.tick(FPS)  # Mostra o novo frame para o jogador

    if Sair==1:
        state=QUIT
    else:
        pygame.mixer.music.unload()
        state=OVER
    return state, ganhador, g_img