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

#SPRITES MAPAS(1-4):
BLOCK1_MAP1 = 'bloco1_mapa1'
BLOCK2_MAP1= 'bloco2_mapa1'
BLOCK3_MAP1 = 'bloco3_mapa1 '

BLOCK1_MAP2 = 'bloco1_mapa2'
BLOCK2_MAP2 = 'bloco2_mapa2'
BLOCK3_MAP2 = 'bloco3_mapa2'

BLOCK1_MAP3 = 'bloco1_mapa3'
BLOCK2_MAP3 = 'bloco2_mapa3'

BLOCK1_MAP4 = 'bloco1_mapa4'
BLOCK2_MAP4 = 'bloco2_mapa4'


BULLET_IMG= 'img_bala'
BARRA_IMG= 'img_bar'
MINIMAP1_IMG= 'minimap_1_bar'
MINIMAP2_IMG= 'minimap_2_bar'
MINIMAP3_IMG= 'minimap_3_bar'
MINIMAP4_IMG= 'minimap_4_bar'



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
    assets[PLAYER1_IMG]=pygame.image.load(os.path.join(IMG_DIR,'player1.png'))
    assets[PLAYER1_IMG]=pygame.transform.scale(assets[PLAYER1_IMG], (PLAYERS_WIDTH, PLAYERS_HEIGHT))

    assets[PLAYER2_IMG]=pygame.image.load(os.path.join(IMG_DIR,'player2.png'))
    assets[PLAYER2_IMG]=pygame.transform.scale(assets[PLAYER2_IMG], (PLAYERS_WIDTH, PLAYERS_HEIGHT))

    assets[PLAYER3_IMG]=pygame.image.load(os.path.join(IMG_DIR,'player3.png'))
    assets[PLAYER3_IMG]=pygame.transform.scale(assets[PLAYER3_IMG], (PLAYERS_WIDTH, PLAYERS_HEIGHT))

    assets[PLAYER4_IMG]=pygame.image.load(os.path.join(IMG_DIR,'player4.png'))
    assets[PLAYER4_IMG]=pygame.transform.scale(assets[PLAYER4_IMG], (PLAYERS_WIDTH, PLAYERS_HEIGHT))

  




 #MAPA 1:
    assets[BLOCK1_MAP1]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa1.png'))
    assets[BLOCK1_MAP1]=pygame.transform.scale(assets[BLOCK1_MAP1], (BLOCK_SIZE, BLOCK_SIZE))

    assets[BLOCK2_MAP1]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa1.png'))
    assets[BLOCK2_MAP1]=pygame.transform.scale(assets[BLOCK2_MAP1], (BLOCK_SIZE, BLOCK_SIZE))
    
 #MAPA 2:
    assets[BLOCK1_MAP2]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa2.png'))
    assets[BLOCK1_MAP2]=pygame.transform.scale(assets[BLOCK1_MAP2], (BLOCK_SIZE, BLOCK_SIZE))

    assets[BLOCK2_MAP2]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa2.png'))
    assets[BLOCK2_MAP2]=pygame.transform.scale(assets[BLOCK2_MAP2], (BLOCK_SIZE, BLOCK_SIZE))

    assets[BLOCK3_MAP2]=pygame.image.load(os.path.join(IMG_DIR,'bloco3mapa2.png'))
    assets[BLOCK3_MAP2]=pygame.transform.scale(assets[BLOCK3_MAP2], (BLOCK_SIZE, BLOCK_SIZE))

 #MAPA 3:
    assets[BLOCK1_MAP3]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa3.png'))
    assets[BLOCK1_MAP3]=pygame.transform.scale(assets[BLOCK1_MAP3], (BLOCK_SIZE, BLOCK_SIZE))

    assets[BLOCK2_MAP3]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa3.png'))
    assets[BLOCK2_MAP3]=pygame.transform.scale(assets[BLOCK2_MAP3], (BLOCK_SIZE, BLOCK_SIZE))



 #MAPA 4: 
    assets[BLOCK1_MAP4]=pygame.image.load(os.path.join(IMG_DIR,'bloco1mapa4.png'))
    assets[BLOCK1_MAP4]=pygame.transform.scale(assets[BLOCK1_MAP4], (BLOCK_SIZE, BLOCK_SIZE))

    assets[BLOCK2_MAP4]=pygame.image.load(os.path.join(IMG_DIR,'bloco2mapa4.png'))
    assets[BLOCK2_MAP4]=pygame.transform.scale(assets[BLOCK2_MAP4], (BLOCK_SIZE, BLOCK_SIZE))

 #BALA:
    assets[BULLET_IMG]=pygame.image.load(os.path.join(IMG_DIR,'bullet.png'))
    assets[BULLET_IMG]=pygame.transform.scale(assets[BULLET_IMG], (BULLET_WIDTH,BULLET_HEIGHT))

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

    return assets