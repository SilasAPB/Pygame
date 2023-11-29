import pygame
import os
from jogo1 import*
from config import *

#DEFINE NOME DOS SPRITES PARA FACILITAR A ULTILIZAÇÃO DO DICIONÁRIO ASSETS(DEFINIDO DENTRO DA FUNÇÃO LOAD_ASSETS):

#SPRITES DOS BACKGROUND:
BACKGROUND = 'backgroud'
BACKGROUND2 = 'background2'
BACKGROUND3 = 'background3'
BACKGROUND4 = 'background4'

#SPRITES DOS PLAYERS:
PLAYER1_IMG = 'player_1_img'
PLAYER2_IMG = 'player_2_img'
PLAYER3_IMG = 'player_3_img'
PLAYER4_IMG = 'player_4_img'

PLAYER1_IMG_L = 'player_1_img_L'
PLAYER2_IMG_L = 'player_2_img_L'
PLAYER3_IMG_L = 'player_3_img_L'
PLAYER4_IMG_L = 'player_4_img_L'

#SPRITES MAPAS(1-4):
MAPS = [
     ['bloco1_mapa1','bloco2_mapa1','bloco3_mapa1'],
     ['bloco1_mapa2','bloco2_mapa2','bloco3_mapa2'],
     ['bloco1_mapa3','bloco2_mapa3','bloco3_mapa3'],
     ['bloco1_mapa4','bloco2_mapa4','bloco3_mapa4']
     ]
BLOCK1_MAP1 = 'bloco1_mapa1'
BLOCK2_MAP1= 'bloco2_mapa1'
BLOCK3_MAP1 = 'bloco3_mapa1'

BLOCK1_MAP2 = 'bloco1_mapa2'
BLOCK2_MAP2 = 'bloco2_mapa2'
BLOCK3_MAP2 = 'bloco3_mapa2'

BLOCK1_MAP3 = 'bloco1_mapa3'
BLOCK2_MAP3 = 'bloco2_mapa3'

BLOCK1_MAP4 = 'bloco1_mapa4'
BLOCK2_MAP4 = 'bloco2_mapa4'


BULLET_STRAIGHT= 'Bullets1'
BULLET_OBLIQUE= 'Bullets2'
BULLET_BOUNCE= 'Bullets3'
BARRA_IMG= 'img_bar'
MINIMAP1_IMG= 'minimap_1_bar'
MINIMAP2_IMG= 'minimap_2_bar'
MINIMAP3_IMG= 'minimap_3_bar'
MINIMAP4_IMG= 'minimap_4_bar'

ARMA1= 'Armas1.png'
ARMA2= 'Armas2.png'
ARMA3= 'Armas3.png'
ARMA4= 'Armas4.png'
ARMA5= 'Armas5.png'
ARMA6= 'Armas6.png'
ARMA7= 'Armas7.png'
ARMA8= 'Armas8.png'
ARMA9= 'Armas9.png'



def load_assets():
    assets ={}

 #DEFINE OS VALORES DO DICIONARIO:

 #BACKGROUNDS:
    assets[BACKGROUND]=pygame.image.load(os.path.join(IMG_DIR, 'background.gif')).convert()
    assets[BACKGROUND]=pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[BACKGROUND2]=pygame.image.load(os.path.join(IMG_DIR, 'mapa2.png')).convert()
    assets[BACKGROUND2]=pygame.transform.scale(assets[BACKGROUND2], (WIDTH, HEIGHT))

    assets[BACKGROUND3]=pygame.image.load(os.path.join(IMG_DIR, 'mapa3.png')).convert()
    assets[BACKGROUND3]=pygame.transform.scale(assets[BACKGROUND3], (WIDTH, HEIGHT))

    assets[BACKGROUND4]=pygame.image.load(os.path.join(IMG_DIR, 'mapa4.png')).convert()
    assets[BACKGROUND4]=pygame.transform.scale(assets[BACKGROUND4], (WIDTH, HEIGHT))

 #PLAYERS:
    assets[PLAYER1_IMG_L]=pygame.image.load(os.path.join(IMG_DIR,'P1F1.png'))
    assets[PLAYER1_IMG_L]=pygame.transform.scale(assets[PLAYER1_IMG_L], (PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L))

    assets[PLAYER2_IMG_L]=pygame.image.load(os.path.join(IMG_DIR,'P2F2.png'))
    assets[PLAYER2_IMG_L]=pygame.transform.scale(assets[PLAYER2_IMG_L], (PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L))

    assets[PLAYER3_IMG_L]=pygame.image.load(os.path.join(IMG_DIR,'P3F3.png'))
    assets[PLAYER3_IMG_L]=pygame.transform.scale(assets[PLAYER3_IMG_L], (PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L))

    assets[PLAYER4_IMG_L]=pygame.image.load(os.path.join(IMG_DIR,'P4F4.png'))
    assets[PLAYER4_IMG_L]=pygame.transform.scale(assets[PLAYER4_IMG_L], (PLAYERS_WIDTH_L, PLAYERS_HEIGHT_L))

  




 #MAPA 1:
    assets[MAPS[0][0]]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa1.png'))
    assets[MAPS[0][0]]=pygame.transform.scale(assets[BLOCK1_MAP1], (BLOCK_SIZE, BLOCK_SIZE))

    assets[MAPS[0][1]]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa1.png'))
    assets[MAPS[0][1]]=pygame.transform.scale(assets[BLOCK2_MAP1], (BLOCK_SIZE, BLOCK_SIZE))
    
 #MAPA 2:
    assets[MAPS[1][0]]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa2.png'))
    assets[MAPS[1][0]]=pygame.transform.scale(assets[BLOCK1_MAP2], (BLOCK_SIZE, BLOCK_SIZE))

    assets[MAPS[1][1]]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa2.png'))
    assets[MAPS[1][1]]=pygame.transform.scale(assets[BLOCK2_MAP2], (BLOCK_SIZE, BLOCK_SIZE))

    assets[MAPS[1][2]]=pygame.image.load(os.path.join(IMG_DIR,'bloco3mapa2.png'))
    assets[MAPS[1][2]]=pygame.transform.scale(assets[BLOCK3_MAP2], (BLOCK_SIZE, BLOCK_SIZE))

 #MAPA 3:
    assets[MAPS[2][0]]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa3.png'))
    assets[MAPS[2][0]]=pygame.transform.scale(assets[BLOCK1_MAP3], (BLOCK_SIZE, BLOCK_SIZE))

    assets[MAPS[2][1]]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa3.png'))
    assets[MAPS[2][1]]=pygame.transform.scale(assets[BLOCK2_MAP3], (BLOCK_SIZE, BLOCK_SIZE))


 #MAPA 4: 
    assets[MAPS[3][0]]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa4.png'))
    assets[MAPS[3][0]]=pygame.transform.scale(assets[BLOCK1_MAP4], (BLOCK_SIZE, BLOCK_SIZE))

    assets[MAPS[3][1]]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa4.png'))
    assets[MAPS[3][1]]=pygame.transform.scale(assets[BLOCK2_MAP4], (BLOCK_SIZE, BLOCK_SIZE))

 #BALAS:
    assets[BULLET_STRAIGHT]=pygame.image.load(os.path.join(IMG_DIR,'Bullets1.png'))
    assets[BULLET_STRAIGHT]=pygame.transform.scale(assets[BULLET_STRAIGHT], (BULLET_SIZE,BULLET_SIZE))
    
    assets[BULLET_OBLIQUE]=pygame.image.load(os.path.join(IMG_DIR,'Bullets2.png'))
    assets[BULLET_OBLIQUE]=pygame.transform.scale(assets[BULLET_OBLIQUE], (BULLET_SIZE,BULLET_SIZE))
    
    assets[BULLET_BOUNCE]=pygame.image.load(os.path.join(IMG_DIR,'Bullets3.png'))
    assets[BULLET_BOUNCE]=pygame.transform.scale(assets[BULLET_BOUNCE], (BULLET_SIZE,BULLET_SIZE))

 #HEALTH BAR:
    assets[BARRA_IMG]=pygame.image.load(os.path.join(IMG_DIR,'health_bar (2).png'))
    assets[BARRA_IMG]=pygame.transform.scale(assets[BARRA_IMG],(BARRA_WIDTH, BARRA_HEIGHT))

 #MINIMAPAS:
    assets[MINIMAP1_IMG]=pygame.image.load(os.path.join(IMG_DIR,'background.gif'))
    assets[MINIMAP1_IMG]=pygame.transform.scale(assets[MINIMAP1_IMG],(MIN_MAP_W, MIN_MAP_H))

    assets[MINIMAP2_IMG]=pygame.image.load(os.path.join(IMG_DIR,'mapa2.png'))
    assets[MINIMAP2_IMG]=pygame.transform.scale(assets[MINIMAP2_IMG],(MIN_MAP_W, MIN_MAP_H))

    assets[MINIMAP3_IMG]=pygame.image.load(os.path.join(IMG_DIR,'mapa3.png'))
    assets[MINIMAP3_IMG]=pygame.transform.scale(assets[MINIMAP3_IMG],(MIN_MAP_W, MIN_MAP_H))

    assets[MINIMAP4_IMG]=pygame.image.load(os.path.join(IMG_DIR,'mapa4.png'))
    assets[MINIMAP4_IMG]=pygame.transform.scale(assets[MINIMAP4_IMG],(MIN_MAP_W, MIN_MAP_H))



   # Armas
    assets['Armas1']=pygame.image.load(os.path.join(IMG_DIR,'Armas1.png'))
    assets['Armas1']=pygame.transform.scale(assets['Armas1'],(GUN_SIZE, GUN_SIZE))
    
    assets['Armas2']=pygame.image.load(os.path.join(IMG_DIR,'Armas2.png'))
    assets['Armas2']=pygame.transform.scale(assets['Armas2'],(GUN_SIZE, GUN_SIZE))
    
    assets['Armas3']=pygame.image.load(os.path.join(IMG_DIR,'Armas3.png'))
    assets['Armas3']=pygame.transform.scale(assets['Armas3'],(GUN_SIZE, GUN_SIZE))
    
    assets['Armas4']=pygame.image.load(os.path.join(IMG_DIR,'Armas4.png'))
    assets['Armas4']=pygame.transform.scale(assets['Armas4'],(GUN_SIZE, GUN_SIZE))

    assets['Armas5']=pygame.image.load(os.path.join(IMG_DIR,'Armas5.png'))
    assets['Armas5']=pygame.transform.scale(assets['Armas5'],(GUN_SIZE, GUN_SIZE))

    assets['Armas6']=pygame.image.load(os.path.join(IMG_DIR,'Armas6.png'))
    assets['Armas6']=pygame.transform.scale(assets['Armas6'],(GUN_SIZE, GUN_SIZE))

    assets['Armas7']=pygame.image.load(os.path.join(IMG_DIR,'Armas7.png'))
    assets['Armas7']=pygame.transform.scale(assets['Armas7'],(GUN_SIZE, GUN_SIZE))

    assets['Armas8']=pygame.image.load(os.path.join(IMG_DIR,'Armas8.png'))
    assets['Armas8']=pygame.transform.scale(assets['Armas8'],(GUN_SIZE, GUN_SIZE))

    assets['Armas9']=pygame.image.load(os.path.join(IMG_DIR,'Armas9.png'))
    assets['Armas9']=pygame.transform.scale(assets['Armas9'],(GUN_SIZE, GUN_SIZE))
    player1=[]
    for i in range(7):
         # Os arquivos de animação são numerados de 00 a 08
         filename = os.path.join(IMG_DIR, 'P1F{}.png'.format(i+1))
         img = pygame.image.load(filename)
         img = pygame.transform.scale(img, (PLAYERS_WIDTH, PLAYERS_HEIGHT))
         player1.append(img)

    assets[PLAYER1_IMG] = player1


    player2=[]
    for i in range(7):
         # Os arquivos de animação são numerados de 00 a 08
         filename = os.path.join(IMG_DIR, 'P2F{}.png'.format(i+1))
         img = pygame.image.load(filename)
         img = pygame.transform.scale(img, (PLAYERS_WIDTH, PLAYERS_HEIGHT))
         player2.append(img)

    assets[PLAYER2_IMG] = player2


    player3=[]
    for i in range(7):
         # Os arquivos de animação são numerados de 00 a 08
         filename = os.path.join(IMG_DIR, 'P3F{}.png'.format(i+1))
         img = pygame.image.load(filename)
         img = pygame.transform.scale(img, (PLAYERS_WIDTH, PLAYERS_HEIGHT))
         player3.append(img)

    assets[PLAYER3_IMG] = player3

    player4=[]
    for i in range(7):
         # Os arquivos de animação são numerados de 00 a 08
         filename = os.path.join(IMG_DIR, 'P4F{}.png'.format(i+1))
         img = pygame.image.load(filename)
         img = pygame.transform.scale(img, (PLAYERS_WIDTH, PLAYERS_HEIGHT))
         player4.append(img)

    assets[PLAYER4_IMG] = player4



    return assets